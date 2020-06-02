from django import forms
from .models import *


class BUnitsForm(forms.ModelForm):

    class Meta:
        model = BUnit
        exclude = [""]
