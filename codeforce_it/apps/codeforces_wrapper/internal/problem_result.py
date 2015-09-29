from codeforce_it.apps.codeforces_wrapper.models import Submission


__author__ = 'Andrew Kuchev (kuchevad@gmail.com)'


class ProblemResult:
    def __init__(self, points, rejected_attempt_count, best_submission_time):
        self.points = points
        self.rejected_attempt_count = rejected_attempt_count
        self.best_submission_time = best_submission_time

    @staticmethod
    def from_problem_submissions(contest, problem, author):
        submissions = list(problem.submission_set.filter(author=author).exclude(
            verdict__in=[Submission.VERDICT_TESTING, Submission.VERDICT_COMPILATION_ERROR]))

        first_correct_submission = next((s for s in submissions if s.verdict == Submission.VERDICT_OK), None)
        minutes_before_problem_was_solved = (
            (first_correct_submission.creation_time - contest.start_time).seconds // 60 if first_correct_submission
            else 0)

        penalty = (len(submissions) - 1) * 50
        points = max(problem.max_score - problem.max_score / 250 * minutes_before_problem_was_solved - penalty,
                     problem.max_score * 0.3) if first_correct_submission else 0
        rejected_attempt_count = sum(1 for s in submissions if s.verdict != Submission.VERDICT_OK)

        return ProblemResult(points, rejected_attempt_count, minutes_before_problem_was_solved)
