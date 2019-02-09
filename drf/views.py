from django.shortcuts import render
from .serializers import PollSerializer
from rest_framework import viewsets
from poll.models import PollModel


class PollViewSet(viewsets.ModelViewSet):
    queryset = PollModel.objects.all()
    serializer_class = PollSerializer

