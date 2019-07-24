import enum

import websocket
from django.db import models
from django.db.models.signals import pre_save, pre_delete, post_save, post_delete
from django.dispatch import receiver


class EnumChoice(enum.Enum):
    @classmethod
    def choices(cls):
        return ((obj.name, obj.value) for obj in cls)

class CommonModel(models.Model):
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __init__(self, *args, **kwargs):
        pre_save.connect(self.save_signal, sender=self.__class__)
        post_save.connect(self.save_signal, sender=self.__class__)

        pre_delete.connect(self.delete_signal, sender=self.__class__)
        post_delete.connect(self.delete_signal, sender=self.__class__)

        return super().__init__(*args, **kwargs)

    
    def save_signal(sender, **kwargs):
        import pdb; pdb.set_trace()

    def delete_signal(sender, **kwargs):
        pass


    class Meta:
        abstract = True
