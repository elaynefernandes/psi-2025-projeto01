from django.urls import path 
from . import viwes

urlpatterns = [
    path('', views.index, name="index"),
]
