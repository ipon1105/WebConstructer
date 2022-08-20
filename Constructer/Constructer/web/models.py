from django.contrib.auth.models import AbstractUser
from django.db.models import JSONField
from django.db import models
import uuid


class User(AbstractUser):
    pass


class Project(models.Model):
    user_id = models.UUIDField(primary_key=False, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=25)
    data = JSONField()

    def __str__(self):
        return self.user_id
        pass

    pass
