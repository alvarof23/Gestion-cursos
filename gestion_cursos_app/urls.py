from django.urls import path
from . import views

urlpatterns = [
    path('curso', views.listar_cursos, name='listar_cursos'),
]