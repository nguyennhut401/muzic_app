import enum
import json

import websocket
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.core import serializers
from django.db import models
from django.db.models.signals import (post_delete, post_save, pre_save)
from django.dispatch import receiver
from django.conf import settings



class EnumChoice(enum.Enum):
    @classmethod
    def choices(cls):
        return ((obj.name, obj.value) for obj in cls)

class CommonModel(models.Model):
    previous_inst = None

    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __init__(self, *args, **kwargs):
        post_save.connect(self.save_signal, sender=self.__class__)
        post_delete.connect(self.delete_signal, sender=self.__class__)

        pre_save.connect(self.pre_save_signal, sender=self.__class__)

        return super().__init__(*args, **kwargs)


    def pre_save_signal(self, sender, **kwargs):
        instance = kwargs['instance']

        self.previous_inst = instance

    
    def save_signal(self, sender, **kwargs):
        channel_layer = get_channel_layer()

        async_to_sync(channel_layer.group_send)(settings.DB_TABLE_SOCKET, {
            'package': self.build_signal_object(kwargs['instance'], 'save')
        })

    def delete_signal(self, sender, **kwargs):
        channel_layer = get_channel_layer()

        async_to_sync(channel_layer.group_send)(settings.DB_TABLE_SOCKET, {
            'package': self.build_signal_object(kwargs['instance'], 'delete')
        })

    def build_signal_object(self, instance, action):
        package_obj = {
            'table': instance.__class__.__name__,
            'action': action,
            'detail': {
                'from': serializers.serialize('json', [self.previous_inst]),
                'to': serializers.serialize('json', [instance])
            }
        }

        return json.dumps(package_obj)

    class Meta:
        abstract = True
