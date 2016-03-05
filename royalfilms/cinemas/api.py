from .serializers import CinemaSerializer
from .models import Cinema

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import permissions


class CinemaList(generics.ListAPIView):
    """
    API class for list all Cinemas from a thread, or create a new Cinema.
    """
    # permission_classes = (permissions.IsAdminUser,)
    queryset = Cinema.objects.all()
    serializer_class = CinemaSerializer