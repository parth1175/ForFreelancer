from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class data(models.Model):
    user = models.CharField(max_length=100, default = 'Missing')
    Website = models.CharField(max_length=100, default = 'Missing')
    Url = models.CharField(max_length=1000, default = 'Missing')
    Company = models.CharField(max_length=1000, default = 'Missing')
    Job = models.CharField(max_length=1000, default = 'Missing')
    Description = models.CharField(max_length=100000, default = 'Missing')
    Notes =  models.CharField(max_length=10000, default = '')
    Applied = models.CharField(max_length=1000, default='Missing')
    Date = models.DateTimeField(default=timezone.now)

