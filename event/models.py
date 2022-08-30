from turtle import title
from django.db import models

from utils.validators import validate_renaming_days


# Create your models here.
class HackathonCounter(models.Model):
    title = models.CharField(max_length=50)
    days_remaining = models.PositiveSmallIntegerField(
        validators=[validate_renaming_days], 
        default=0
    )

    def __str__(self):
        return f"{self.title} - {self.days_renaming}"