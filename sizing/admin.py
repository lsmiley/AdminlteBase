from django.contrib import admin

from .models import Sizing, SizingItem
# Register your models here.

admin.site.register(Sizing)
admin.site.register(SizingItem)
