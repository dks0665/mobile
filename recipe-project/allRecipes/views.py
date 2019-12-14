from django.shortcuts import render
from .models import allRecipes

# Create your views here.

def allRecipes(request):
    allRecipes = allRecipes.objects
    return render(request, 'allblogs.html', {'allRecipes':allRecipes})