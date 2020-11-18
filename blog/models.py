from django.db import models
from django.utils import timezone

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=60, unique=True, null=False)
    headline = models.CharField(max_length=60)
    body = models.TextField(max_length=500)
    heading_img_link = models.CharField(max_length=200, blank=False)
    sub_img_link_1 = models.CharField(max_length=200, blank=True)
    sub_img_link_2 = models.CharField(max_length=200, blank=True)
    sub_img_link_3 = models.CharField(max_length=200, blank=True)
    sub_img_link_4 = models.CharField(max_length=200, blank=True)
    sub_img_link_5 = models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.title