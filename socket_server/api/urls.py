from django.urls import path, include

from rest_framework import routers
from . import viewsets

router = routers.SimpleRouter()
router.register('room', viewsets.RoomViewSet, basename='room')
router.register('device', viewsets.DeviceViewSet, basename='device')

urlpatterns = [
    path('', include(router.urls))
]