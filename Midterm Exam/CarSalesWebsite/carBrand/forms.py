from django import forms
from .models import carBrand


class carBrandForm(forms.ModelForm):
    class Meta:
        model=carBrand
        fields='__all__'