from django.db import models

class registration(models.Model):
    name = models.CharField(max_length=100)
    last = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    text =  models.CharField(max_length=500)
