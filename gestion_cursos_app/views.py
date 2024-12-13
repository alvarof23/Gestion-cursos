from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Curso
from .forms import curso_form

# Vista para listar todos los cursos
def listar_cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'cursos/listar_cursos.html', {'cursos': cursos})

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

