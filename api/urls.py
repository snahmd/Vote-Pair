from django.urls import path, include
from rest_framework import routers
from .views import PixelCoinViewSet, PhotoPairViewSet, VoteViewSet

router = routers.DefaultRouter()
router.register('pixelcoin', PixelCoinViewSet)
router.register('photopair', PhotoPairViewSet)
router.register('vote', VoteViewSet)

urlpatterns = [
    path('', include(router.urls))
]