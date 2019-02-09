from rest_framework import serializers
from poll.models import PollModel


class PollSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PollModel
        fields = ('title', 'description', 'url_logo')

