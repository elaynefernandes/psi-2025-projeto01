from django.urls import path 
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('sobre/', views.sobre, name="sobre"),
    path('elenco/', views.elenco, name="elenco"),
    path('diario/', views.diario, name="diario"),
]
