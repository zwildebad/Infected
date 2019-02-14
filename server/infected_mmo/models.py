from django.db import models

# Create your models here.


class User(models.Model):
    user_id = models.AutoField(primary_key=True, unique=True, null=False)
    username = models.CharField(max_length=60, unique=True)
    wins = models.IntegerField(default=0, null=False)
    kills = models.IntegerField(default=0, null=False)
    infected = models.IntegerField(default=0, null=False)
    def __str__(self):
        return self.username
