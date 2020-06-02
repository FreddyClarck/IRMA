from django import forms
from .models import *


class TUnitsForm(forms.ModelForm):

    class Meta:
        model = TUnit
        exclude = [""]
