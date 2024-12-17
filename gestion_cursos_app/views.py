from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Curso, Estudiante, Inscripcion
from .forms import curso_form, estudiante_form, inscripcion_form

# Vista para listar todos los cursos
def listar_cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'gestion_cursos_app/cursos/listar_cursos.html', {'cursos': cursos})

# Vista para crear un nuevo curso
def crear_curso(request):
    if request.method == 'POST':
        form = curso_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_cursos')
    else:
        form = curso_form()
    return render(request, 'cursos/crear_curso.html', {'form': form})

# Vista para editar un curso
def editar_curso(request, pk):
    curso = get_object_or_404(Curso, pk=pk)
    if request.method == 'POST':
        form = curso_form(request.POST, instance=curso)
        if form.is_valid():
            form.save()
            return redirect('listar_cursos')
    else:
        form = curso_form(instance=curso)
    return render(request, 'cursos/editar_curso.html', {'form': form})

# Vista para eliminar un curso
def eliminar_curso(request, pk):
    curso = get_object_or_404(Curso, pk=pk)
    curso.delete()
    return redirect('listar_cursos')

#Vista para crear un nuevo estudiante
def crear_estudiante(request):
    if request.method == 'POST':
        form = estudiante_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_estudiantes')
    else:
        form = estudiante_form()
    return render(request, 'estudiantes/crear_estudiante.html', {'form': form})

#Vista para listar todos los estudiantes
def listar_estudiantes(request):
    estudiantes = Estudiante.objects.all()
    return render(request, 'gestion_cursos_app/estudiantes/listar_estudiantes.html', {'estudiantes': estudiantes})

#Vista para editar un estudiante
def editar_estudiante(request, pk):
    estudiante = get_object_or_404(Estudiante, pk=pk)
    if request.method == 'POST':
        form = estudiante_form(request.POST, instance=estudiante)
        if form.is_valid():
            form.save()
            return redirect('listar_estudiantes')
    else:
        form = estudiante_form(instance=estudiante)
    return render(request, 'estudiantes/editar_estudiante.html', {'form': form})

#Vista para eliminar un estudiante
def eliminar_estudiante(request, pk):
    estudiante = get_object_or_404(Estudiante, pk=pk)
    estudiante.delete()
    return redirect('listar_estudiantes')

#Vista para crear una inscripcion
def crear_inscripcion(request):
    if request.method == 'POST':
        form = inscripcion_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_inscripciones')
    else:
        form = inscripcion_form()
    return render(request, 'inscripciones/crear_inscripcion.html', {'form': form})

#Vista para listar todas las inscripciones
def listar_inscripciones(request):
    inscripciones = Inscripcion.objects.all()
    return render(request, 'gestion_cursos_app/inscripciones/listar_inscripciones.html', {'inscripciones': inscripciones})

#Vista para eliminar una inscripcion
def eliminar_inscripcion(request, pk):
    inscripcion = get_object_or_404(Inscripcion, pk=pk)
    inscripcion.delete()
    return redirect('listar_inscripciones')