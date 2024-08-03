from django.contrib import admin
from .models import Accessory

@admin.register(Accessory)
class AccessoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'pin_number')
