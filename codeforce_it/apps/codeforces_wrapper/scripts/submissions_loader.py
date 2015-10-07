from itertools import groupby, chain
from datetime import datetime
import time

from codeforces import CodeforcesAPI, VerdictType
from django.utils.timezone import make_aware, get_default_timezone

from codeforce_it.apps.codeforces_wrapper.models import Submission


__author__ = 'Andrew Kuchev (kuchevad@gmail.com)'


def group_by_to_dict_of_sets(iterable, key=None, value_selector=None):
    value_selector = value_selector or (lambda x: x)
    return dict(map(lambda k_v: (k_v[0], set(map(value_selector, k_v[1]))), groupby(iterable, key=key)))


def retrieve_contest_submissions(contest):
    problems = group_by_to_dict_of_sets(contest.problem_set.order_by('cf_contest_id'),
                                        key=lambda p: p.cf_contest_id,
                                        value_selector=lambda p: p.cf_index)
    return list(
        chain.from_iterable(map(lambda contestant: retrieve_contestant_submissions(contestant, contest, problems),
                                contest.contestants.all())))


def store_only_new_submissions(contest, submissions):
    if submissions:
        first_submission = min(submissions, key=lambda s: s.creation_time)
        first_submission_creation_time = make_aware(datetime.fromtimestamp(first_submission.creation_time),
                                                    get_default_timezone())
        stored_submission_ids = set(map(lambda s: s.cf_id,
                                        Submission.objects.filter(creation_time__gte=first_submission_creation_time)))
        for submission in filter(lambda s: s.id not in stored_submission_ids, submissions):
            problem = contest.problem_set.get(cf_contest_id=submission.problem.contest_id,
                                              cf_index=submission.problem.index)
            author = contest.contestants.get(cf_handle=submission.author.members[0].handle)
            Submission.from_cf_submission(submission, problem, author).save()


def load_submissions_to_db(contests):
    for contest in contests:
        submissions = retrieve_contest_submissions(contest)
        store_only_new_submissions(contest, submissions)


def retrieve_contestant_submissions(contestant, contest, problem_indices_by_contest_id):
    time.sleep(1)
    api = CodeforcesAPI()
    return list(filter(lambda s: (make_aware(datetime.fromtimestamp(s.creation_time),
                                             get_default_timezone()) >= contest.start_time and
                                  s.verdict != VerdictType.testing and
                                  s.problem.index in problem_indices_by_contest_id.get(s.problem.contest_id, [])),
                       api.user_status(contestant.cf_handle)))
