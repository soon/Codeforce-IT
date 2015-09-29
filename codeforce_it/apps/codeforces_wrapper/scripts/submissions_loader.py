from itertools import groupby, chain
import operator
from datetime import datetime

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


def store_only_new_submissions(submissions):
    if submissions:
        first_submission = min(submissions, key=lambda s: s.creation_time)
        stored_submission_ids = set(map(operator.itemgetter('cf_id'),
                                        Submission.objects.filter(creation_time__gte=first_submission.creation_time)))
        for submission in filter(lambda s: s.id not in stored_submission_ids, submissions):
            Submission.from_json(submission).save()


def load_submissions_to_db(contests):
    for c in contests:
        submissions = retrieve_contest_submissions(c)
        store_only_new_submissions(submissions)


def retrieve_contestant_submissions(contestant, contest, problem_indices_by_contest_id):
    api = CodeforcesAPI()
    return list(filter(lambda s: (make_aware(datetime.fromtimestamp(s.creation_time),
                                             get_default_timezone()) >= make_aware(contest.start_time,
                                                                                   get_default_timezone()) and
                                  s.verdict != VerdictType.testing and
                                  s.problem.index in problem_indices_by_contest_id.get(s.problem.contest_id, [])),
                       api.user_status(contestant.cf_handle)))
