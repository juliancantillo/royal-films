from django.shortcuts import get_object_or_404

from .serializers import CinemaSerializer, ShowtimesSerializer,\
        FunctionSerializer, ShowSerializer, CinemaFunctionsSerializer
from .models import Cinema, Function

from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.decorators import detail_route, list_route

class CinemaViewSet(viewsets.ModelViewSet):
    """
    API class for list all Cinemas from a thread, or create a new Cinema.
    """
    queryset = Cinema.objects.all()
    lookup_field = 'uuid'
    serializer_class = CinemaSerializer

    @detail_route(methods=['get'])
    def movies(self, request, uuid=None):
        cinema = self.get_object()

        serializer = CinemaFunctionsSerializer(cinema)

        return Response(serializer.data)

class ShowtimesView(generics.ListAPIView):

    queryset = Function.objects.all()
    lookup_field = 'movie__uuid'
    lookup_url_kwarg = 'uuid'
    serializer_class = ShowtimesSerializer

    def get_queryset(self):
        if 'uuid' in self.kwargs:
            return Function.objects.filter(
                movie__uuid=self.kwargs['uuid']
                )

        return Function.objects.all()
