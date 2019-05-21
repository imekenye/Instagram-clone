from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth


# Create your views here.

# def home(request):
#     return render(request, 'instapp/home.html')

def home(request):
        return render(request, 'instapp/home.html')


def feed(request):
    return render(request, 'instapp/feed.html')
