from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class data(models.Model):
    user = models.CharField(max_length=100, default = '1')
    url = models.CharField(max_length=100, default = 'www.error.com')
    Company = models.CharField(max_length=100, default = 'ApplyAway')
    Job = models.CharField(max_length=100, default = 'Error')
    Description = models.CharField(max_length=10000, default = 'Great Company')
    Notes =  models.CharField(max_length=10000, default = ' ')