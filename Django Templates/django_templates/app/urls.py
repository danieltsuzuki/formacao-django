from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('aprender', views.aprender, name='aprender'),
    path('numero/<int:num>', views.numero, name='numero'),
]