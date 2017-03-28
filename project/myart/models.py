from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    name = models.TextField(max_length=50, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    pic= models.ImageField(upload_to = 'documents/', default = 'documents/None/no-img.jpg')

class Msg(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    checked = models.BooleanField(default=False)
    
class Painting(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, unique=False,on_delete=models.CASCADE)
    title = models.CharField(max_length=30, blank=True)
    painting = models.ImageField(upload_to = 'paintings/', default = 'paintings/None/no-img.jpg')
