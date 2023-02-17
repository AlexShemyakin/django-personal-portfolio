from django.contrib import admin
from .models import Project

class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'title',
        'description',
    )
    search_fields = ('title',)
    empty_value_display = '-пусто-'

admin.site.register(Project, ProjectAdmin)

