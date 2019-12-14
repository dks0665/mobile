from django.shortcuts import render ,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .models import Main

# Create your views here.
def home(request):
    # return render(request, 'home.html')
    homes = Main.objects
    return render(request, 'home.html', {'homes':homes})

def all(request):
    alls = Main.objects
    return render(request, 'all.html', {'alls':alls})