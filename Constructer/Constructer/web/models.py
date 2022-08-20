from django.contrib.auth.models import AbstractUser
from django.db.models import JSONField
from django.db import models


class User(AbstractUser):
    pass


class CustomJsonField(models.JSONField):
    def from_db_value(self, value, expression, connection):
        if isinstance(value, dict):
            return value
        return super().from_db_value(value, expression, connection)


class Project(models.Model):
    user_id = models.BigIntegerField(primary_key=False)
    title = models.CharField(max_length=25)
    data = CustomJsonField(default={'div':'div'})

    def __str__(self):
        return self.user_id
        pass

    pass
