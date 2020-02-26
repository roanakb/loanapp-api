from django.db import models
from django.contrib.postgres.fields import JSONField

class Business(models.Model):
    name = models.CharField(max_length=100)
    data = JSONField()

class Owner(models.Model):
    name = models.CharField(max_length=100)
    data = JSONField()
    business = models.ForeignKey(Business)
