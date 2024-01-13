from django import forms
from .models import CarModel,Comment


class carForm(forms.ModelForm):
    class Meta:
        model=CarModel
        fields='__all__'


class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=['name','email','body']
