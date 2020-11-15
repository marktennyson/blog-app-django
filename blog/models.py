from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=60, unique=True)
    headline = models.CharField(max_length=60)
    body = models.TextField(max_length=500)
    def __str__(self):
        return self.title