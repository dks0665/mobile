from django.shortcuts import render ,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .models import Main

def home(request):
    # return render(request, 'home.html')
    homes = Main.objects.all
    return render(request, 'home.html', {'homes':homes})

def all(request):
    alls = Main.objects.all
    return render(request, 'all.html', {'alls':alls})

def recipe1(request):
    recipes1 = Main.objects.all
    return render(request, 'recipe1.html', {'recipes1':recipes1})

def recipe2(request):
    recipes2 = Main.objects.all
    return render(request, 'recipe2.html', {'recipes2':recipes2})

def recipe3(request):
    recipes3 = Main.objects.all
    return render(request, 'recipe3.html', {'recipes3':recipes3})

def recipe4(request):
    recipes4 = Main.objects.all
    return render(request, 'recipe4.html', {'recipes4':recipes4})

