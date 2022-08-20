from django.contrib.auth.models import AbstractUser
from django.db.models import JSONField
from django.db import models


class User(AbstractUser):
    pass


class Project2(models.Model):
    user_id = models.BigIntegerField(primary_key=False)
    title = models.CharField(max_length=25)
    data = JSONField()


    def __str__(self):
        return self.user_id
        pass

    pass