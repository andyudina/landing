from django.db import models

# Create your models here.

class Lead(models.Model):
    email = models.EmailField()
