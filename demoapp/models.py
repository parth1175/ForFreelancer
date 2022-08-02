from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class data(models.Model):
    user = models.CharField(max_length=100, default = 'missing')
    Website = models.CharField(max_length=100, default = 'missing')
    Url = models.CharField(max_length=1000, default = 'missing')
    Company = models.CharField(max_length=1000, default = 'missing')
    Job = models.CharField(max_length=1000, default = 'missing')
    Description = models.CharField(max_length=100000, default = 'missing')
    Notes =  models.CharField(max_length=10000, default = '')
    Applied = models.CharField(max_length=1000, default='missing')
    Date = models.DateTimeField(default=timezone.now)

