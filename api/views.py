from django.shortcuts import render
from rest_framework import viewsets, status
from .models import PixelCoin, PhotoPair, Vote
from .serializers import PixelCoinSerializer, PhotoPairSerializer, VoteSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

# Create your views here.

class PixelCoinViewSet(viewsets.ModelViewSet):
    queryset = PixelCoin.objects.all()
    serializer_class = PixelCoinSerializer


class PhotoPairViewSet(viewsets.ModelViewSet):
    queryset = PhotoPair.objects.all()
    serializer_class = PhotoPairSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        

        serializer.is_valid(raise_exception=True)
        
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
   

class VoteViewSet(viewsets.ModelViewSet):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer