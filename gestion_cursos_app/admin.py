from django.contrib import admin
from .models import Inscripcion, Curso, Estudiante

# Register your models here.
admin.site.register(Inscripcion)
admin.site.register(Curso)
admin.site.register(Estudiante)