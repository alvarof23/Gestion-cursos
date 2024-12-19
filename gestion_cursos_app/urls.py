from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('curso/', ListarCursos.as_view(), name='listar_curso'),
    path('curso/crear/', CrearCurso.as_view(), name='crear_curso'),
    path('curso/editar/<int:pk>/', EditarCurso.as_view(), name='editar_curso'),
    path('curso/eliminar/<int:pk>/', EliminarCurso.as_view(), name='eliminar_curso'),


    path('', views.principal, name='principal'),

    # path('curso/', views.listar_cursos, name='listar_curso'),
    # path('curso/crear/', views.crear_curso, name='crear_curso'),
    # path('curso/editar/<int:pk>/', views.editar_curso, name='editar_curso'),
    # path('curso/eliminar/<int:pk>/', views.eliminar_curso, name='eliminar_curso'),
    
    path('estudiante/', views.listar_estudiantes, name='listar_estudiante'),
    path('estudiante/crear/', views.crear_estudiante, name='crear_estudiante'),
    path('estudiante/editar/<int:pk>/', views.editar_estudiante, name='editar_estudiante'),
    path('estudiante/eliminar/<int:pk>/', views.eliminar_estudiante, name='eliminar_estudiante'),

    path('inscritos/', views.listar_inscripciones, name='listar_inscripcion'),
    path('inscritos/new/', views.crear_inscripcion, name='crear_inscripcion'),
    path('inscritos/del/<int:pk>/', views.eliminar_inscripcion, name='eliminar_inscripcion'),
]