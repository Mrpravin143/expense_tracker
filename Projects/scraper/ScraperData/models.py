from django.db import models

# Create your models here.

class News(models.Model):
    titel = models.CharField(max_length=1000)
    description = models.TextField()
    images = models.URLField(max_length=2000)
    external_link = models.URLField(max_length=2000)
