from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import  AuthenticationForm
from django.contrib.auth import logout
from django.shortcuts import redirect

from .forms import UserForm


def home(request):
    return render(request, 'users/home.html')
