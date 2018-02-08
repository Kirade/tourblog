from django.contrib import admin
from .models import Column, Comment, Tag


@admin.register(Column)
class ColumnAdmin(admin.ModelAdmin):
    pass


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass
