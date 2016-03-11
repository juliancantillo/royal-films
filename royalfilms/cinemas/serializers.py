from rest_framework import serializers
from .models import Cinema, Function, Show, FunctionType, Auditorium

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



class CinemaSerializer(serializers.ModelSerializer):
    """
    Serializer for Cinema Model
    """
    uuid = serializers.UUIDField(format='hex')

    class Meta:
        model = Cinema
        fields = ('uuid','name','address','lat','lng',)



class FunctionTypeSerializer(serializers.ModelSerializer):
    """
    Serializer for Function type Model
    """
    uuid = serializers.UUIDField(source='auditorium.uuid', format='hex')
    showtimes = ShowSerializer(source='show_set', many=True, read_only=True)

    class Meta:
        model = FunctionType
        fields = ('uuid','is_3D','showtimes',)



class FunctionSerializer(serializers.ModelSerializer):
    """
    Serializer for Function Model
    """
    uuid = serializers.UUIDField(source='movie.uuid', format='hex')
    movie = ShowtimeMovieSerializer(many=False, read_only=True)
    group = FunctionTypeSerializer(source='functiontype_set', many=True, read_only=True)

    class Meta:
        model = Function
        fields = ('uuid','movie','group')


class ShowtimesSerializer(serializers.ModelSerializer):
    """
    Serializer for Function Model
    """
    uuid = serializers.UUIDField(source='movie.uuid', format='hex')
    movie = ShowtimeMovieSerializer(many=False, read_only=True)
    cinema = CinemaSerializer(many=False, read_only=True)
    group = FunctionTypeSerializer(source='functiontype_set', many=True, read_only=True)

    class Meta:
        model = Function
        fields = ('uuid','movie','cinema','group')



class CinemaFunctionsSerializer(serializers.ModelSerializer):
    """
    Serializer for Cinema Model
    """
    uuid = serializers.UUIDField(format='hex')
    functions = FunctionSerializer(source='function_set', read_only=True, many=True)

    class Meta:
        model = Cinema
        fields = ('uuid','name','functions','address','lat','lng',)

