from django.contrib import admin
from django.utils.html import format_html
from .models import Slider, Team
import uuid

# Register your models here.

class TeamAdmin(admin.ModelAdmin):

    def _id(self, object):
        return format_html(f"{str(uuid.uuid4())[:7]} ---> {object.id}")
    
    def myphoto(self, object):
        return format_html(f"<img src='{object.photo.url}' width='40' />")

    list_display = ['_id', 'myphoto', 'first_name', 'last_name', 'role', 'created_date']
    list_display_links = ['_id', 'myphoto', 'first_name', 'last_name']
    search_fields = ['first_name', 'last_name', 'role', 'created_date']
    list_filter = ['role']

admin.site.register(Slider)
admin.site.register(Team, TeamAdmin)


