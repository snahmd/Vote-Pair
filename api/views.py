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
        ###
        credit = PixelCoin.objects.get(user=request.user).credit
        if credit < 10:
            return Response({'error': 'You do not have enough credits to create a new photo pair'}, status=status.HTTP_400_BAD_REQUEST)
        ####
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
   

class VoteViewSet(viewsets.ModelViewSet):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        ### Increase the credit of the user who voted by 1
        
        user = request.user
        pixel_coin = PixelCoin.objects.get(user=user)
        pixel_coin.credit += 1
        pixel_coin.save()

        ####
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
