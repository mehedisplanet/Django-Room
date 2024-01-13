from django import forms
from . import models


class StudentForm(forms.ModelForm):
    class Meta:
        model = models.StudentModel
        fields = '__all__'
        labels = {
            'name': 'Student Name',
            'roll': 'Student Roll',
            'fatherName': 'Father Name'
        }
        widgets = {
            'name': forms.TextInput(attrs={'class' : 'btn-danger'}),
            # 'roll': forms.PasswordInput()
        }
        help_texts={
            'name': "Write your full name",
        }
        error_messages={
            'name': {'required': 'your name is required'},
        }
