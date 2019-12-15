"""recipe URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path ,include
from django.conf import settings
from django.conf.urls.static import static
import main.views
import login.views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',main.views.home, name = 'home'),
    # path('main/', include('main.urls')),
    path('home', main.views.home, name='homePage'),
    path('all', main.views.all, name='allPage'),
    path('recipe1', main.views.recipe1, name='recipe1Page'),
    path('recipe2', main.views.recipe2, name='recipe2Page'),
    path('recipe3', main.views.recipe3, name='recipe3Page'),
    path('recipe4', main.views.recipe4, name='recipe4Page'),
    path('recipe5', main.views.recipe5, name='recipe5Page'),
    path('recipe6', main.views.recipe6, name='recipe6Page'),
    path('recipe7', main.views.recipe7, name='recipe7Page'),
    path('recipe8', main.views.recipe8, name='recipe8Page'),
    path('login/', include('login.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
