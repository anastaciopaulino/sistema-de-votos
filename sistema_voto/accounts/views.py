from django.shortcuts import render
from django.views import generic
from accounts import models

# Create your views here.

class Sigin(generic.CreateView):
    model = models.User

