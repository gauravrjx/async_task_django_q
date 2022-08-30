from django_q.models import Schedule
from django.db.models import F, Case, When  # `Case` and `when` required for conditional expressions
'''

# just like `switch cases
# example:

Client.objects.annotate(
...     discount=Case(
...         When(account_type=Client.GOLD, then=Value('5%')),
...         When(account_type=Client.PLATINUM, then=Value('10%')),
...         default=Value('0%'),
...     ),
... ).values_list('name', 'discount')

<QuerySet [('Jane Doe', '0%'), ('James Smith', '5%'), ('Jack Black', '10%')]>
'''

from .models import HackathonCounter


def decement_hackathoncounter_value():
    """
    decrement `days_remaining` by one, if its value is greater than one
    else, do nothing. Also, set default value of it to zero
    """
    HackathonCounter.objects.update(
        days_renaming=Case(
            When(days_remaining__gt=0, then=F("days_remaining")-1),
            default=0
        )
    )

Schedule.objects.create(
    func="decement_hackathoncounter_value",
    schedule_type=Schedule.DAILY,
)

if __name__ == "__main__":

    # schedule the task
    # either we can schedule it from here, or can create own custom command to schedule the task
    # I have
    Schedule.objects.create(
        func="decement_hackathoncounter_value",
        schedule_type=Schedule.DAILY,
    )
