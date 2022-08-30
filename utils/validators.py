import datetime
import re
from rest_framework import serializers

from django.utils.translation import gettext as _


def validate_renaming_days(days):
    if not days > 0:
        raise serializers.ValidationError(
            _("Remaining day(s) must be at least one!"))
    return days
