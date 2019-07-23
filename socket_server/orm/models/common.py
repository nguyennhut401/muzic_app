from django.db import models

import enum

class EnumChoice(enum.Enum):
    @classmethod
    def choices(cls):
        return ((obj.name, obj.value) for obj in cls)

class CommonModel(models.Model):
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        abstract = True