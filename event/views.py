from os import sync
import sys

from django.shortcuts import render

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django_q.tasks import async_task, result


from .models import HackathonCounter
from .serializers import EventSerializer
from utils import hooks


class CreateCounterView(APIView):

    serializer_class = EventSerializer

    def post(self, request, *args, **kwargs):
        """
        Create and save new `hackathon` event and then 
        create and perform two async tasks 
        1. send `hackathon` cretion notification on console
        2. sleep for 5 seconds
        """
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            # TODO create new event and send notification email
            serializer.save()

            # send email
            # msg = "a new hackathon reminder has been created"
            # async_task(
            #     "django.core.mail.send_mail",
            #     "New Hackathon created",
            #     msg,
            #     "from@example.com",
            #     ["to1@example.com", "to2@example.com"],
            # )


            # ------------------- task `first`
            async_task("time.sleep", 10, hook=hooks.print_first_task_result, sync=True)

            # ------------------- task `second`
            async_task("time.sleep", 5, hook=hooks.print_second_task_result)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
