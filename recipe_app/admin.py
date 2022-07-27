from django.contrib import admin

from .models import recipe

class appAdmin(admin.ModelAdmin):

    list_display = ("name", "cuisine",)

# Register your models here.
admin.site.register(recipe,appAdmin)
