from django.urls import path
from . import views

urlpatterns = [
    path('', views.Cursos, name='Cursos')
]