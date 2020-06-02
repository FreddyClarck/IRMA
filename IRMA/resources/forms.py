from django import forms
from .models import *


class InstrumentsForm(forms.ModelForm):

    class Meta:
        model = Instrument
        exclude = [""]
