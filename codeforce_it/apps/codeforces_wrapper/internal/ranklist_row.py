from codeforce_it.apps.codeforces_wrapper.internal.problem_result import ProblemResult


__author__ = 'Andrew Kuchev (kuchevad@gmail.com)'


class RanklistRow:
    def __init__(self, contestant, problem_results):
        self.contestant = contestant
        self.problem_results = problem_results
        self.total_score = sum(r.points for r in problem_results)

    @staticmethod
    def from_contest_problems(contest, author):
        return RanklistRow(author, [ProblemResult.from_problem_submissions(contest, problem, author)
                                    for problem in contest.problem_set.all()])
