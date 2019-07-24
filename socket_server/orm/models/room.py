import uuid

from django.contrib.auth.models import User
from django.db import models

from . import common


class Room(common.CommonModel):
    class Status(common.EnumChoice):
        ONL = 'Online'
        OFF = 'OffLine'
        DIS = 'Deactivated'

    uuid = models.TextField(unique=True, db_index=True)
    member = models.ManyToManyField(User)
    status = models.CharField(max_length=10, default=Status.OFF.name, choices=Status.choices())

    @staticmethod
    def generate_room_id():
        return uuid.uuid4()

    class Meta:
        db_table='chat_group'
