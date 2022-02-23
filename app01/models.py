from django.db import models

# Create your models here.
class UserInfo(models.Model):
    name = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    plan = models.CharField(max_length=20, default="none")
    age = models.IntegerField()