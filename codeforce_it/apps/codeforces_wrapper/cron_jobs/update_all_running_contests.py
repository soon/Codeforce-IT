from django_cron import CronJobBase, Schedule

from codeforce_it.apps.codeforces_wrapper.models import Contest
from codeforce_it.apps.codeforces_wrapper.scripts.submissions_loader import load_submissions_to_db


__author__ = 'Andrew Kuchev (kuchevad@gmail.com)'


class UpdateAllRunningContests(CronJobBase):
    RUN_EVERY_MINS = 1

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'codeforces_wrapper.update_all_running_contests'

    def do(self):
        running_contests = Contest.get_running_contests()
        load_submissions_to_db(running_contests)
