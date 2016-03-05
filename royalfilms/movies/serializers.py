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