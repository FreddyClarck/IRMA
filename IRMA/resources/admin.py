from django.contrib import admin
from .models import *


class InstrumentAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Instrument._meta.fields]
    list_filter = [field.name for field in Instrument._meta.fields]
    search_fields = [field.name for field in Instrument._meta.fields]

    class Meta:
        model = Instrument


admin.site.register(Instrument, InstrumentAdmin)
