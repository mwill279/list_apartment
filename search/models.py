from django.db import models

# Create your models here.

class Result (models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    

