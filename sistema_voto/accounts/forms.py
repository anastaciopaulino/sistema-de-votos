from django import forms
from accounts.models import User, UserOthersInfo
from django.contrib import auth

class UserForm(forms.ModelForm):
    class Meta():
        model = User
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2', 'email')
    

class UserOthersInfoForm(forms.ModelForm):
    class Meta():
        model = UserOthersInfo
        fields = ('bi')

    def __init__(self):
        self.fields['bi'].labe = 'Número do B.I: '
