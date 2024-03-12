from rest_framework import serializers
from .models import PixelCoin, PhotoPair, Vote
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class PixelCoinSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = PixelCoin
        fields = ['id', 'user', 'credit', 'created_date']
       

class PhotoPairSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = PhotoPair
        fields = ['id', 'user', 'content1', 'content2', 'created_date']

class VoteSerializer(serializers.ModelSerializer):  
    user = UserSerializer()
    photo_pair = PhotoPairSerializer()
    class Meta:
        model = Vote
        fields = ['id', 'user', 'photo_pair', 'vote', 'created_date']         