from django.urls import path

from . import views

urlpatterns = [
    path('download', views.download, name='index'),
    path('', views.homepage, name='index'),
]