from django.shortcuts import render ,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .models import Notice

# Create your views here.

def main(request):
    # return render(request, 'home.html')
    mains = Notice.objects.all
    return render(request, 'main.html', {'mains':mains})