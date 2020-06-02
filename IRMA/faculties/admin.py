from django.contrib import admin
from .models import *


class TUnitAdmin(admin.ModelAdmin):
    list_display = [field.name for field in TUnit._meta.fields]
    list_filter = [field.name for field in TUnit._meta.fields]
    search_fields = [field.name for field in TUnit._meta.fields]

    class Meta:
        model = TUnit


admin.site.register(TUnit, TUnitAdmin)
