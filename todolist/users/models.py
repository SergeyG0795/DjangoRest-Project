from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    birthday = models.DateField()
    email = models.CharField(max_length=100)
