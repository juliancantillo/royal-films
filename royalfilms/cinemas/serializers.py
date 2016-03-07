from rest_framework import serializers
from .models import Cinema, Function, Show

from royalfilms.movies.models import Movie
from royalfilms.movies.serializers import MovieSerializer,\
    ShowtimeMovieSerializer



class ShowSerializer(serializers.ModelSerializer):
    """
    Serializer for Show Model
    """
    time = serializers.TimeField(read_only=True, format='%I:%M %p')

    class Meta:
        model = Show
        fields = ('time',)

class FunctionSerializer(serializers.ModelSerializer):
    """
    Serializer for Function Model
    """
    uuid = serializers.UUIDField(source='movie.uuid', format='hex')
    title = serializers.CharField(source='movie.title', read_only=True)
    showtimes = ShowSerializer(source='show_set', many=True, read_only=True)

    class Meta:
        model = Function
        fields = ('uuid','title', 'showtimes')

class CinemaSerializer(serializers.ModelSerializer):
    """
    Serializer for Cinema Model
    """
    uuid = serializers.UUIDField(format='hex')
    # functions = FunctionSerializer(source='function_set', read_only=True, many=True)
    # url = serializers.URLField(source='get_absolute_url', read_only=True)

    class Meta:
        model = Cinema
        fields = ('uuid','name','address','lat','lng',)

class CinemaFunctionsSerializer(serializers.ModelSerializer):
    """
    Serializer for Cinema Model
    """
    uuid = serializers.UUIDField(format='hex')
    functions = FunctionSerializer(source='function_set', read_only=True, many=True)
    # url = serializers.URLField(source='get_absolute_url', read_only=True)

    class Meta:
        model = Cinema
        fields = ('uuid','name','functions','address','lat','lng',)


class ShowtimesSerializer(serializers.ModelSerializer):
    """
    Serializer for Function Model
    """
    uuid = serializers.UUIDField(format='hex')
    movie = ShowtimeMovieSerializer(many=False, read_only=True)
    cinema = CinemaSerializer(many=False, read_only=True)
    showtimes = ShowSerializer(source='show_set', many=True, read_only=True)

    class Meta:
        model = Function
        fields = ('uuid','cinema','movie','showtimes')
