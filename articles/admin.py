from django.contrib import admin
from articles.models import *


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display=[field.name for field in Comment._meta.fields]

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display=[field.name for field in Article._meta.fields]
    # filter_horizontal = ['comment']
