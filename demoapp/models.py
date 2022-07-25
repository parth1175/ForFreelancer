from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class data(models.Model):
    user = models.CharField(max_length=100, default = '1')
    user2 = models.CharField(max_length=100, default='2')
    Website = models.CharField(max_length=100, default = 'LinkedIn')
    Url = models.CharField(max_length=1000, default = 'www.error.com')
    Company = models.CharField(max_length=1000, default = 'ApplyAway')
    Job = models.CharField(max_length=1000, default = 'Error')
    Description = models.CharField(max_length=100000, default = 'Great Company')
    Notes =  models.CharField(max_length=10000, default = 'Nothing')
    Applied = models.CharField(max_length=1000, default='Nothing')
    Date = models.DateTimeField(default=timezone.now)
