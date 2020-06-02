from django import forms
from .models import *


class EmployeesForm(forms.ModelForm):

    class Meta:
        model = Employee
        exclude = [""]
