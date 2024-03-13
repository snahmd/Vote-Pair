from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class PixelCoin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='pixel_coin')
    credit = models.IntegerField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username + ' has ' + str(self.credit) + ' credits'
    
class PhotoPair(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content1 = models.TextField()
    content2 = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content1 + ' vs ' + self.content2
    
class Vote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    photo_pair = models.ForeignKey(PhotoPair, on_delete=models.CASCADE)
    vote = models.IntegerField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username + ' voted ' + str(self.vote) + ' for ' + self.photo_pair.content1 + ' vs ' + self.photo_pair.content2   
    
