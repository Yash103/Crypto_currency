from django import forms
from .models import Reg

class RegistrationForm(forms.ModelForm):

    class Meta:
         model = Reg
         fields = '__all__'
         
class LoginForm(forms.Form):
    username=forms.CharField(max_length=30)
    password=forms.CharField(max_length=30)

