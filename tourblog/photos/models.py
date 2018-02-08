from django.db import models
from django.conf import settings


class Photo(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=20)
    content = models.CharField(max_length=100, blank=True)
    photo = models.ImageField(upload_to='photo/%Y/%m/%d')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
