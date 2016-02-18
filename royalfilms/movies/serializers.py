from rest_framework import serializers
from .models import Movie


class MovieSerializer(serializers.ModelSerializer):
    """
    Serializaer for Movie Model
    """
    class Meta:
        model = Movie