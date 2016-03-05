from rest_framework import serializers
from .models import Cinema, Function, Show

from royalfilms.movies.serializers import MovieSerializer



class ShowSerializer(serializers.ModelSerializer):
    """
    Serializaer for Show Model
    """
    time = serializers.TimeField(read_only=True, format='%I:%M %p')
    
    # url = serializers.URLField(source='get_absolute_url', read_only=True)
    
    class Meta:
        model = Show
        fields = ('time',)

class FunctionSerializer(serializers.ModelSerializer):
    """
    Serializaer for Function Model
    """
    title = serializers.CharField(source='movie.title', read_only=True)
    showtimes = ShowSerializer(source='show_set', many=True, read_only=True)
    # time = serializers.TimeField(read_only=True, format='%I:%M %p')
    
    # url = serializers.URLField(source='get_absolute_url', read_only=True)
    
    class Meta:
        model = Function
        fields = ('title', 'showtimes')

class CinemaSerializer(serializers.ModelSerializer):
    """
    Serializaer for Cinema Model
    """
    uuid = serializers.UUIDField(format='hex')
    functions = FunctionSerializer(source='function_set', read_only=True, many=True)
    # url = serializers.URLField(source='get_absolute_url', read_only=True)
    
    class Meta:
        model = Cinema
        fields = ('uuid','name','functions','address','lat','lng',)