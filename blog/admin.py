from django.contrib import admin
from .models import Blog


class BlogAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'title',
        'description',
        'date',
    )
    search_fields = ('title',)
    list_filter = ('date',)
    empty_value_display = '-пусто-'

admin.site.register(Blog, BlogAdmin)
