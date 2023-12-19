from django import forms
from django.core import validators

# widgets == field to html input


class contactForm(forms.Form):
    name = forms.CharField(label="Full Name : ", help_text="Total length must be 100 word", required=True, disabled=False,
                           widget=forms.Textarea(attrs={'id': 'text_area', 'class': 'class1', 'placeholder': 'Enter your name'}))
    # file=forms.FileField()
    email = forms.EmailField(label='User Email')
    # age=forms.IntegerField()
    age = forms.CharField(widget=forms.NumberInput)
    # weight=forms.FloatField()
    # balance=forms.DecimalField()
    check = forms.BooleanField()
    birthday = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    appointment = forms.DateTimeField(
        widget=forms.DateInput(attrs={'type': 'datetime-local'}))
    CHOICES = [('Small', 'Small'), ('Medium', 'Medium'), ('Large', 'Large')]
    size = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    meal = [('Pepperoni', 'Pepperoni'),
            ('Mushroom', 'Mushroom'), ('Beef', 'Beef')]
    pizza = forms.MultipleChoiceField(
        choices=meal, widget=forms.CheckboxSelectMultiple)

# class StudentData(forms.Form):
#     name=forms.CharField(widget=forms.TextInput)
#     email=forms.EmailField(widget=forms.EmailInput)

#     # def clean_name(self):
#     #     valName=self.cleaned_data['name']
#     #     if len(valName)<10:
#     #         raise forms.ValidationError('Enter a name with at least 10 characters')
#     #     return valName
#     # def clean_email(self):
#     #     valEmail=self.cleaned_data['email']
#     #     if '.com' not in valEmail:
#     #         raise forms.ValidationError('Your email must contain .com')
#     #     return valEmail

#     def clean(self):
#         cleaned_data=super().clean()
#         valName=self.cleaned_data['name']
#         valEmail=self.cleaned_data['email']
#         if len(valName)<10:
#             raise forms.ValidationError('Enter a name with at least 10 characters')
#         if '.com' not in valEmail:
#             raise forms.ValidationError('Your email must contain .com')


class StudentData(forms.Form):
    name = forms.CharField(widget=forms.TextInput, validators=[
                           validators.MinLengthValidator(10, message='Enter a name with at least 10 characters')])
    email = forms.EmailField(widget=forms.EmailInput, validators=[
                             validators.EmailValidator])
    age = forms.IntegerField(
        validators=[validators.MaxValueValidator(35), validators.MinValueValidator(18)])
    file = forms.FileField(
        validators=[validators.FileExtensionValidator(allowed_extensions=['pdf','png'])])
    
class passwordMatching(forms.Form):
    name=forms.CharField(widget=forms.TextInput)
    password=forms.CharField(widget=forms.PasswordInput)
    confirm_password=forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data=super().clean()
        valPass=self.cleaned_data['password']
        valCon=self.cleaned_data['confirm_password']
        if valCon != valPass:
            raise forms.ValidationError("Password doesn't Match")