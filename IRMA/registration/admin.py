from django.contrib import admin
from .models import *


class EmployeeAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Employee._meta.fields]
    list_filter = [field.name for field in Employee._meta.fields]
    search_fields = [field.name for field in Employee._meta.fields]

    class Meta:
        model = Employee


admin.site.register(Employee, EmployeeAdmin)
