from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse


class Photo(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=20)
    content = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to='photo/%Y/%m/%d')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('photos:detail', args=[self.id])


class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
    related_name='photo_comment_set')
    photo = models.ForeignKey(Photo, related_name='photo_comment_set')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content

    def get_absolute_url(self):
        return reverse('photo:detail', args=[self.photo.id])
