from django.contrib import admin
from .models import *


class BUnitAdmin(admin.ModelAdmin):
    list_display = [field.name for field in BUnit._meta.fields]
    list_filter = [field.name for field in BUnit._meta.fields]
    search_fields = [field.name for field in BUnit._meta.fields]

    class Meta:
        model = BUnit


admin.site.register(BUnit, BUnitAdmin)
