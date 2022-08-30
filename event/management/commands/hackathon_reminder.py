from django.core.management.base import BaseCommand
from django_q.models import Schedule
from django_q.tasks import schedule


class Command(BaseCommand):
    """
    ~ custom command to schudle the task
    ~ command will be same as the file name `hackathon_reminder`
    ~ can be run as `python manage.py hackathon_reminder`
    """

    # can be accessed as `python manage.py hackathon_reminder --help`
    help = "Create a CRON job"

    def handle(self, *args, **options):
        schedule(
            name="Decrement `Remaining Days` by one for `Hackathon Event`",
            func="event.tasks.decement_hackathoncounter_value",
            schedule_type='M', # `M` -> `Minute`, `H` -> `Hours`
        )
        self.stdout.write(self.style.SUCCESS("CRON job created successfully!"))