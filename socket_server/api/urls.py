from django.urls import path, include

from rest_framework import routers
from . import viewsets

router = routers.SimpleRouter()
router.register('room', viewsets.RoomViewSet, basename='room')

urlpatterns = [
    path('', include(router.urls))
]