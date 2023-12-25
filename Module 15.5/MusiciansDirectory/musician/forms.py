from django import forms
from .models import musicianModel

class musicianForm(forms.ModelForm):
    class Meta:
        model=musicianModel
        fields="__all__"