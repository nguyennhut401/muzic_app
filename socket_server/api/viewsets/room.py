from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from orm.models import Room

from ..serializers import RoomSerializer


class RoomViewSet(viewsets.ModelViewSet):
    serializer_class = RoomSerializer
    queryset = Room.objects.all()

    @action(methods=['POST'], detail=False)
    def register(self, request):
        user = request.user

        room_id = Room.generate_room_id()

        return Response({
            'room_id': room_id
        }, status=status.HTTP_200_OK)
