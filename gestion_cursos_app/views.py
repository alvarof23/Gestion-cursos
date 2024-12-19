from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Curso, Estudiante, Inscripcion
from .forms import curso_form, estudiante_form, inscripcion_form
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

class ListarCursos(ListView):
    model=Curso
    template_name='gestion_cursos_app/cursos/listar_cursos.html'
    context_object_name='cursos'
class CrearCurso(CreateView):
    model=Curso
    template_name='gestion_cursos_app/cursos/crear_cursos.html'
    form_class=curso_form
    success_url=reverse_lazy('listar_curso')
class EditarCurso(UpdateView):
    model=Curso
    template_name='gestion_cursos_app/cursos/editar_cursos.html'
    form_class=curso_form
    success_url=reverse_lazy('listar_curso')
class EliminarCurso(DeleteView):
    model=Curso
    template_name='gestion_cursos_app/cursos/eliminar_cursos.html'
    success_url=reverse_lazy('listar_curso')

# Vista principal
def principal(request):
    return render(request, 'gestion_cursos_app/principal.html')

# # Vista para listar todos los cursos
# def listar_cursos(request):
#     cursos = Curso.objects.all()
#     return render(request, 'gestion_cursos_app/cursos/listar_cursos.html', {'cursos': cursos})

# # Vista para crear un nuevo curso
# def crear_curso(request):
#     if request.method == 'POST':
#         form = curso_form(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('listar_curso')
#     else:
#         form = curso_form()
#     return render(request, 'gestion_cursos_app/cursos/crear_cursos.html', {'form': form})

# # Vista para editar un curso
# def editar_curso(request, pk):
#     curso = get_object_or_404(Curso, pk=pk)
#     if request.method == 'POST':
#         form = curso_form(request.POST, instance=curso)
#         if form.is_valid():
#             form.save()
#             return redirect('listar_curso')
#     else:
#         form = curso_form(instance=curso)
#     return render(request, 'gestion_cursos_app/cursos/editar_cursos.html', {'form': form})

# Vista para eliminar un curso
def eliminar_curso(request, pk):
    curso = get_object_or_404(Curso, pk=pk)
    if request.method == "POST":
        curso.delete()
        return redirect('listar_curso')
    else:
        return render(request, 'gestion_cursos_app/cursos/eliminar_cursos.html', {'curso': curso})
    
#Vista para crear un nuevo estudiante
def crear_estudiante(request):
    if request.method == 'POST':
        form = estudiante_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_estudiante')
    else:
        form = estudiante_form()
    return render(request, 'gestion_cursos_app/estudiante/crear_estudiante.html', {'form': form})

#Vista para listar todos los estudiantes
def listar_estudiantes(request):
    estudiantes = Estudiante.objects.all()
    return render(request, 'gestion_cursos_app/estudiante/listar_estudiante.html', {'estudiantes': estudiantes})

#Vista para editar un estudiante
def editar_estudiante(request, pk):
    estudiante = get_object_or_404(Estudiante, pk=pk)
    if request.method == 'POST':
        form = estudiante_form(request.POST, instance=estudiante)
        if form.is_valid():
            form.save()
            return redirect('listar_estudiante')
    else:
        form = estudiante_form(instance=estudiante)
    return render(request, 'gestion_cursos_app/estudiante/editar_estudiante.html', {'form': form})

#Vista para eliminar un estudiante
def eliminar_estudiante(request, pk):
    estudiante = get_object_or_404(Estudiante, pk=pk)
    if request.method == "POST":
        estudiante.delete()
        return redirect('listar_estudiante')
    else:
        return render(request, 'gestion_cursos_app/estudiante/eliminar_estudiante.html', {'estudiante': estudiante})

    
#Vista para crear una inscripcion
def crear_inscripcion(request):
    if request.method == 'POST':
        form = inscripcion_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_inscripcion')
    else:
        form = inscripcion_form()
    return render(request, 'gestion_cursos_app/inscripcion/crear_inscripcion.html', {'form': form})

#Vista para listar todas las inscripciones
def listar_inscripciones(request):
    inscripciones = Inscripcion.objects.all()
    return render(request, 'gestion_cursos_app/inscripcion/listar_inscripcion.html', {'inscripciones': inscripciones})

#Vista para eliminar una inscripcion
def eliminar_inscripcion(request, pk):
    inscripcion = get_object_or_404(Inscripcion, pk=pk)
    if request.method == "POST":
        inscripcion.delete()
        return redirect('listar_inscripcion')
    else:
        return render(request, 'gestion_cursos_app/inscripcion/eliminar_inscripcion.html', {'inscripcion': inscripcion})