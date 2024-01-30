from django.urls import path

from . import views

urlpatterns = [
    path('download', views.download, name='index'),
    path('json_response', views.json_response, name='json_response'),
    path('', views.homepage, name='index'),
]