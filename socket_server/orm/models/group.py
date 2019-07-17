from django.db import models
from django.contrib.auth.models import User

from . import common

class Group(common.CommonModel):
    member = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    
