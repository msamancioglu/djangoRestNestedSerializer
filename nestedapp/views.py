from django.shortcuts import render
from .serializers import AlbumSerializer, TrackSerializer
from .models import Album, Track
from rest_framework import viewsets
# Create your views here.


class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    