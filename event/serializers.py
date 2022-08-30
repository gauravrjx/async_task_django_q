from dataclasses import field
from pyexpat import model
from rest_framework import serializers

from .models import HackathonCounter


class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = HackathonCounter
        fields = ['title', 'days_remaining']