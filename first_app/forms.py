from django import forms
from . import models
import datetime

GENDERS = [
    ('m', 'Male'),
    ('f', 'Female'),
    ('o', 'Other'),
]

class DForm(forms.Form):
    name = forms.CharField(max_length=10)
    value = forms.DecimalField(label='Enter your age')
    email_address = forms.EmailField(label='Enter your email')
    birth_year = forms.DateField(initial=datetime.date.today)
    gender = forms.ChoiceField(choices=GENDERS)

class MForm(forms.ModelForm):
    class Meta:
        model = models.DModel
        fields = '__all__'