from django import forms


class StudentForm(forms.Form):
    roll=forms.IntegerField()
    name=forms.CharField()
    father_name=forms.CharField()
    address=forms.CharField()


class PasswordMatching(forms.Form):
    name=forms.CharField(widget=forms.TextInput)
    password=forms.CharField(widget=forms.PasswordInput)
    rePassword=forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data=super().clean()
        valPass=self.cleaned_data['password']
        valCon=self.cleaned_data['rePassword']
        if valCon != valPass:
            raise forms.ValidationError("Password doesn't Match")


class OfficeForm(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()
    address=forms.CharField()
