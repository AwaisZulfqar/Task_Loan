from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import *


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Email')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2'] 

    def clean(self):
        cleaned_data = super().clean()
        pass1 = cleaned_data.get("password1")
        pass2 = cleaned_data.get("password2")

        if pass2 and pass1 and pass2 != pass1:
            raise forms.ValidationError("Passwords do not match.")
        return cleaned_data
    

class BankForm(forms.ModelForm):
    class Meta:
        model = Bank
        fields = "__all__"
        
