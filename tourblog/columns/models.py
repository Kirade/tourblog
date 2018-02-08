from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse


class Column(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tag_set = models.ManyToManyField('Tag', blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('columns:column_detail', args=[self.id])


class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='column_comment_set')
    column = models.ForeignKey(Column, related_name='column_comment_set')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content

    def get_absolute_url(self):
        return reverse('column:detail', args=[self.column.id])


class Tag(models.Model):
    name = models.CharField(max_length=20)

