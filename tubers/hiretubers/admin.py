from django.contrib import admin
from .models import Hiretuber
# Register your models here.

class HiretuberAdmin(admin.ModelAdmin):
    def full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"


    list_display = ("full_name","email", "tuber_name")


admin.site.register(Hiretuber, HiretuberAdmin)
