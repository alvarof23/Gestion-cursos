from django.urls import path
from . import views

urlpatterns = [
    path('', views.principal, name='principal'),

    path('curso/', views.listar_cursos, name='listar_cursos'),
    path('curso/crear/', views.crear_curso, name='crear_curso'),
    path('curso/editar/<int:pk>/', views.editar_curso, name='editar_curso'),
    path('curso/eliminar/<int:pk>/', views.eliminar_curso, name='eliminar_curso'),
    
    path('estudiante/', views.listar_estudiantes, name='listar_estudiantes'),
    path('estudiante/crear/', views.crear_estudiante, name='crear_estudiante'),
    path('estudiante/editar/<int:pk>/', views.editar_estudiante, name='editar_estudiante'),
    path('estudiante/eliminar/<int:pk>/', views.eliminar_estudiante, name='eliminar_estudiante'),

    path('inscritos/', views.listar_inscripciones, name='listar_inscripciones'),
    path('inscritos/new/', views.crear_inscripcion, name='crear_inscripcion'),
    path('inscritos/del/<int:pk>/', views.eliminar_inscripcion, name='eliminar_inscripcion'),
]