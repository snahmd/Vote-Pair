from django.shortcuts import render
from rest_framework import viewsets
from .models import PixelCoin, PhotoPair, Vote
from .serializers import PixelCoinSerializer, PhotoPairSerializer, VoteSerializer
# Create your views here.

class PixelCoinViewSet(viewsets.ModelViewSet):
    queryset = PixelCoin.objects.all()
    serializer_class = PixelCoinSerializer


class PhotoPairViewSet(viewsets.ModelViewSet):
    queryset = PhotoPair.objects.all()
    serializer_class = PhotoPairSerializer

class VoteViewSet(viewsets.ModelViewSet):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer