from django.db import models

# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=30)
    username =  models.CharField(max_length=50)
    date_joined = models.DateTimeField(blank=True, null=True)
    modpass = models.CharField(max_length=10)
