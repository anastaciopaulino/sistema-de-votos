from django.shortcuts import render
from django.views import generic
from accounts import models
from accounts import forms

# Create your views here.

class SignUp(generic.CreateView):
    model = models.User
    form_class = forms.UserForm
    template_name = 'accounts/signup.html'

