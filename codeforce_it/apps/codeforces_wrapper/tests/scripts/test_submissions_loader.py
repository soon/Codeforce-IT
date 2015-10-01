from unittest import mock
from datetime import datetime
from datetime import timedelta

import codeforces
from django.test import TestCase

from codeforce_it.apps.codeforces_wrapper.models import Contest
from codeforce_it.apps.codeforces_wrapper.scripts.submissions_loader import retrieve_contestant_submissions, \
    store_only_new_submissions, retrieve_contest_submissions
from codeforce_it.apps.codeforces_wrapper import models


__author__ = 'Andrew Kuchev (kuchevad@gmail.com)'


class SubmissionsLoaderTests(TestCase):
    @mock.patch.object(codeforces.CodeforcesAPI, 'user_status')
    def test_retrieve_contestant_submissions(self, mock_user_status):
        mock_user_status.return_value = [
            codeforces.Submission('''{"id":13158455,"contestId":580,"creationTimeSeconds":1442942706,
            "relativeTimeSeconds":3306,"problem":{"contestId":580,"index":"B","name":"Кефа и компания",
            "type":"PROGRAMMING","points":1250.0,"tags":["binary search","sortings","two pointers"]},
            "author":{"contestId":580,"members":[{"handle":"soon"}],
            "participantType":"CONTESTANT","ghost":false,"room":142,"startTimeSeconds":1442939400},
            "programmingLanguage":"GNU C++11","verdict":"OK","testset":"TESTS",
            "passedTestCount":35,"timeConsumedMillis":561,"memoryConsumedBytes":4096000}'''),
            codeforces.Submission('''{"id":13156276,"contestId":580,"creationTimeSeconds":1442942124,
            "relativeTimeSeconds":2724,"problem":{"contestId":580,"index":"C",
            "name":"Кефа и парк","type":"PROGRAMMING","points":1500.0,"tags":["dfs and similar","trees"]},
            "author":{"contestId":580,"members":[{"handle":"soon"}],"participantType":"CONTESTANT","ghost":false,
            "room":142,"startTimeSeconds":1442939400},"programmingLanguage":"GNU C++11","verdict":"OK",
            "testset":"TESTS","passedTestCount":40,"timeConsumedMillis":623,"memoryConsumedBytes":21504000}'''),
            codeforces.Submission('''{"id":13153676,"contestId":580,"creationTimeSeconds":1442941466,
            "relativeTimeSeconds":2066,"problem":{"contestId":580,"index":"C","name":"Кефа и парк",
            "type":"PROGRAMMING","points":1500.0,"tags":["dfs and similar","trees"]},
            "author":{"contestId":580,"members":[{"handle":"soon"}],"participantType":"CONTESTANT","ghost":false,
            "room":142,"startTimeSeconds":1442939400},"programmingLanguage":"GNU C++11","verdict":"WRONG_ANSWER",
            "testset":"PRETESTS","passedTestCount":7,"timeConsumedMillis":15,"memoryConsumedBytes":0}'''),
            codeforces.Submission('''{"id":13148475,"contestId":580,"creationTimeSeconds":1442940297,
            "relativeTimeSeconds":896,"problem":{"contestId":580,"index":"B","name":"Кефа и компания",
            "type":"PROGRAMMING","points":1250.0,"tags":["binary search","sortings","two pointers"]},
            "author":{"contestId":580,"members":[{"handle":"soon"}],"participantType":"CONTESTANT","ghost":false,
            "room":142,"startTimeSeconds":1442939400},"programmingLanguage":"GNU C++11","verdict":"WRONG_ANSWER",
            "testset":"PRETESTS","passedTestCount":13,"timeConsumedMillis":108,"memoryConsumedBytes":512000}'''),
            codeforces.Submission('''{"id":13144872,"contestId":580,"creationTimeSeconds":1442939683,
            "relativeTimeSeconds":283,"problem":{"contestId":580,"index":"A","name":"Кефа и первые шаги",
            "type":"PROGRAMMING","points":750.0,"tags":["brute force","dp","implementation"]},
            "author":{"contestId":580,"members":[{"handle":"soon"}],"participantType":"CONTESTANT","ghost":false,
            "room":142,"startTimeSeconds":1442939400},"programmingLanguage":"GNU C++11","verdict":"OK",
            "testset":"TESTS","passedTestCount":28,"timeConsumedMillis":249,"memoryConsumedBytes":0}''')
        ]

        contestant = models.Contestant.objects.create(cf_handle='soon')
        contest = models.Contest.objects.create(start_time=datetime.fromtimestamp(1442900000),
                                                duration=timedelta(days=7))
        submissions = retrieve_contestant_submissions(contestant, contest, {580: ['A', 'C']})
        self.assertEquals(3, len(submissions))

    def test_store_only_new_submissions__no_submissions(self):
        store_only_new_submissions(Contest(), [])

    @mock.patch.object(codeforces.CodeforcesAPI, 'user_status')
    def test_retrieve_contest_submissions(self, mock_user_status):
        mock_user_status.return_value = [
            codeforces.Submission('''{"id":13158455,"contestId":580,"creationTimeSeconds":1442942706,
            "relativeTimeSeconds":3306,"problem":{"contestId":580,"index":"B","name":"Кефа и компания",
            "type":"PROGRAMMING","points":1250.0,"tags":["binary search","sortings","two pointers"]},
            "author":{"contestId":580,"members":[{"handle":"soon"}],
            "participantType":"CONTESTANT","ghost":false,"room":142,"startTimeSeconds":1442939400},
            "programmingLanguage":"GNU C++11","verdict":"OK","testset":"TESTS",
            "passedTestCount":35,"timeConsumedMillis":561,"memoryConsumedBytes":4096000}'''),
            codeforces.Submission('''{"id":13156276,"contestId":580,"creationTimeSeconds":1442942124,
            "relativeTimeSeconds":2724,"problem":{"contestId":580,"index":"C",
            "name":"Кефа и парк","type":"PROGRAMMING","points":1500.0,"tags":["dfs and similar","trees"]},
            "author":{"contestId":580,"members":[{"handle":"soon"}],"participantType":"CONTESTANT","ghost":false,
            "room":142,"startTimeSeconds":1442939400},"programmingLanguage":"GNU C++11","verdict":"OK",
            "testset":"TESTS","passedTestCount":40,"timeConsumedMillis":623,"memoryConsumedBytes":21504000}'''),
            codeforces.Submission('''{"id":13153676,"contestId":580,"creationTimeSeconds":1442941466,
            "relativeTimeSeconds":2066,"problem":{"contestId":580,"index":"C","name":"Кефа и парк",
            "type":"PROGRAMMING","points":1500.0,"tags":["dfs and similar","trees"]},
            "author":{"contestId":580,"members":[{"handle":"soon"}],"participantType":"CONTESTANT","ghost":false,
            "room":142,"startTimeSeconds":1442939400},"programmingLanguage":"GNU C++11","verdict":"WRONG_ANSWER",
            "testset":"PRETESTS","passedTestCount":7,"timeConsumedMillis":15,"memoryConsumedBytes":0}'''),
            codeforces.Submission('''{"id":13148475,"contestId":580,"creationTimeSeconds":1442940297,
            "relativeTimeSeconds":896,"problem":{"contestId":580,"index":"B","name":"Кефа и компания",
            "type":"PROGRAMMING","points":1250.0,"tags":["binary search","sortings","two pointers"]},
            "author":{"contestId":580,"members":[{"handle":"soon"}],"participantType":"CONTESTANT","ghost":false,
            "room":142,"startTimeSeconds":1442939400},"programmingLanguage":"GNU C++11","verdict":"WRONG_ANSWER",
            "testset":"PRETESTS","passedTestCount":13,"timeConsumedMillis":108,"memoryConsumedBytes":512000}'''),
            codeforces.Submission('''{"id":13144872,"contestId":580,"creationTimeSeconds":1442939683,
            "relativeTimeSeconds":283,"problem":{"contestId":580,"index":"A","name":"Кефа и первые шаги",
            "type":"PROGRAMMING","points":750.0,"tags":["brute force","dp","implementation"]},
            "author":{"contestId":580,"members":[{"handle":"soon"}],"participantType":"CONTESTANT","ghost":false,
            "room":142,"startTimeSeconds":1442939400},"programmingLanguage":"GNU C++11","verdict":"OK",
            "testset":"TESTS","passedTestCount":28,"timeConsumedMillis":249,"memoryConsumedBytes":0}''')
        ]

        contestant = models.Contestant.objects.create(cf_handle='soon')
        contest = models.Contest.objects.create(start_time=datetime.fromtimestamp(1442900000),
                                                duration=timedelta(days=7))
        contest.contestants.add(contestant)

        models.Problem.objects.create(cf_contest_id=580, cf_index='A', max_score=500, contest=contest)
        models.Problem.objects.create(cf_contest_id=580, cf_index='C', max_score=500, contest=contest)

        submissions = retrieve_contest_submissions(contest)

        self.assertIsInstance(submissions, list)
        self.assertEqual(3, len(submissions))
