from django.urls import path

from . import views

urlpatterns = [
    path('download', views.download, name='download'),
    path('save_contact', views.save_contact, name='save_contact'),
    path('', views.homepage, name='index'),
]