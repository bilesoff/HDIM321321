from django.contrib import admin
from .models import Good


@admin.register(Good)
class GoodAdmin(admin.ModelAdmin):
    list_display = ('article', 'manufacturer', 'mark', 'model', 'price', 'is_active')
