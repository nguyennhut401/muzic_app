from rest_framework import viewsets

from ..serializers.device import DeviceSerializer, Device

class DeviceViewSet(viewsets.ModelViewSet):
    serializer_class = DeviceSerializer
    queryset = Device.objects.all()
    