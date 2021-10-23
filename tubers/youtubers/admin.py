from django.contrib import admin
from .models import Youtuber
from django.utils.html import format_html

# Register your models here.


class YoutuberAdmin(admin.ModelAdmin):
    def myphoto(self, object):
        return format_html(f"<img src='{object.photo.url}' width='70' />")

    list_display = ['myphoto', "name", "price", 'subs_count', 'is_featured', "city"]
    list_display_links = ("name", 'myphoto')
    search_fields = [fields.name for fields in Youtuber._meta.get_fields()]
    list_filter = ['is_featured', 'city', 'camera_type']
    list_editable = ('is_featured',)



admin.site.register(Youtuber, YoutuberAdmin)
