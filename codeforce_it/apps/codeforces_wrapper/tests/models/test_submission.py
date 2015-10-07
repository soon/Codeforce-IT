from datetime import timedelta, datetime

from django.test import TestCase
from codeforces import Submission
from django.utils.timezone import now, make_aware, get_default_timezone

from codeforce_it.apps.codeforces_wrapper import models


__author__ = 'Andrew Kuchev (kuchevad@gmail.com)'


class SubmissionTest(TestCase):
    def test_from_cf_submission(self):
        contest = models.Contest.objects.create(start_time=now(), duration=timedelta(hours=2))
        problem = models.Problem.objects.create(cf_contest_id=100119, cf_index='D', max_score=500, contest=contest)
        author = models.Contestant.objects.create(cf_handle='Fefer_Ivan')

        cf_submission = Submission(
            '''{"id": 13004518, "contestId": 100119, "creationTimeSeconds": 1442305802,
            "relativeTimeSeconds": 2147483647,
             "problem": {"contestId": 100119, "index": "D", "name": "Корень кубического уравнения",
                         "type": "PROGRAMMING", "tags": []},
             "author": {"contestId": 100119, "members": [{"handle": "Fefer_Ivan"}], "participantType": "PRACTICE",
                        "ghost": false, "startTimeSeconds": 1352216400}, "programmingLanguage": "GNU C++11",
             "verdict": "OK", "testset": "TESTS", "passedTestCount": 30, "timeConsumedMillis": 30,
             "memoryConsumedBytes": 204800}''')
        submission = models.Submission.from_cf_submission(cf_submission, problem, author)

        self.assertEquals(submission.problem, problem)
        self.assertEquals(submission.author, author)
        self.assertEquals(submission.cf_id, 13004518)
        self.assertEquals(submission.creation_time, make_aware(datetime.fromtimestamp(cf_submission.creation_time),
                                                               get_default_timezone()))
