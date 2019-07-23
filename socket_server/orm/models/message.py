from django.db import models
from django.contrib.auth.models import User

from . import common

class Message(common.CommonModel):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    content = models.TextField()

    class Meta:
        db_table='chat_message'