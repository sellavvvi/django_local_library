from django.db import models
from django.urls import reverse

class Messages(models.Model):
     name = models.CharField(max_length=100)
     email = models.EmailField(max_length=254)
     message = models.TextField()
     time_send = models.DateTimeField(auto_now_add=True)