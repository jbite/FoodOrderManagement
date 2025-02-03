from django.contrib import admin
from . models import Item

# Register your models here.
@admin.register(Item)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ("meal", "status")
    list_filter = ("status",)
    search_fields = ("meal", "description")