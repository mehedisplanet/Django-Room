from django import forms
from .models import taskModel

class taskForm(forms.ModelForm):
    
    class Meta:
        model = taskModel
        fields = "__all__"

        