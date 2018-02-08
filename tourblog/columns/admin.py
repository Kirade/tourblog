from django.contrib import admin
from .models import Column, Comment


@admin.register(Column)
class ColumnAdmin(admin.ModelAdmin):
    pass


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass

