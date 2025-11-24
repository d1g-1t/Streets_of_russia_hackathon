from django.contrib import admin
from .models import BlogPost, PostRegion

from streets_backend.settings import EMPTY_VALUE


@admin.register(BlogPost)
class BlogPostConfig(admin.ModelAdmin):
    list_display = (
        'id',
        'type',
        'title',
        'author',
        'relevance_date',
        'created_at',
        'updated_at'
    )
    empty_value_display = EMPTY_VALUE
    fieldsets = (
        ('Ключевая информация', {
            'fields': ('type', 'title', 'author', 'relevance_date')
        }),
        ('Контент', {
            'fields': ('image', 'content')
        }),
        ('Даты', {
            'fields': ('created_at', 'updated_at')
        })
    )
    readonly_fields = ('created_at', 'updated_at')


@admin.register(PostRegion)
class PostRegionConfig(admin.ModelAdmin):
    ...
