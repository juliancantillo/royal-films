from rest_framework import serializers
from .models import Movie


class MovieSerializer(serializers.ModelSerializer):
    """
    Serializaer for Movie Model
    """
    url = serializers.URLField(source='get_absolute_url', read_only=True)
    uuid = serializers.UUIDField(format='hex')

    class Meta:
        model = Movie

class ShowtimeMovieSerializer(serializers.ModelSerializer):

    uuid = serializers.UUIDField(format='hex')
    url = serializers.URLField(source='get_absolute_url', read_only=True)
    runtime = serializers.CharField(source='display_runtime', read_only=True)

    class Meta:
        model = Movie
        fields = ('uuid','title','url','runtime')
