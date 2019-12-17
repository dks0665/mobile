from django.urls import path
from . import views

urlpatterns = [
	path('', views.main, name='noticeMain'),
    path('notice1/',views.notice1, name='notice1'),
    path('notice2/',views.notice2, name='notice2')
    ]