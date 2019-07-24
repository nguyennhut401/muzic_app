from django.db import models

from . import common

class Device(common.CommonModel):

    class Status(common.EnumChoice):
        ONL = 'Online'
        OFF = 'Offline'
        COR = 'Corrupted'
        DAM = 'Dammaged'

    name = models.CharField(max_length=250, blank=True, null=True)
    token = models.CharField(max_length=255)
    status = models.CharField(max_length=20, choices=Status.choices(), default=Status.OFF.name)
    
    class Meta:
        db_table='device'
