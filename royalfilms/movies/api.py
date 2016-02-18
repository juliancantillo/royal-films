from .serializers import MovieSerializer
from .models import Movie

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import permissions


class MovieList(generics.ListCreateAPIView):
    """
    API class for list all Movies from a thread, or create a new Movie.
    """
    permission_classes = (permissions.IsAdminUser,)
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer