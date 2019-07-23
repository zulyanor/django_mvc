from django import forms
from .models import Hewan

class InputHewan(forms.ModelForm):

    class Meta:
        model = Hewan
        fields = ('nama', 'species')