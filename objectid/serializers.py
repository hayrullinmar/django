from rest_framework import serializers
from .models import Artwork


class ArtworkSerializer(serializers.Serializer)
    class Meta:
        model = Artwork
        field = ['owner', ]
