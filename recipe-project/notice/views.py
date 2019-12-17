from django.shortcuts import render ,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .models import Notice

# Create your views here.

def main(request):
    mains = Notice.objects.all
    return render(request, 'main.html', {'mains':mains})

def notice1(request):
    notice1 = Notice.objects.all
    return render(request, 'notice1.html', {'notice1':notice1})

def notice2(request):
    notice2 = Notice.objects.all
    return render(request, 'notice2.html', {'notice2':notice2})