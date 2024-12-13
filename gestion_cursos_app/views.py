from django.shortcuts import render

# Create your views here.
def Cursos (request):
    return render(request,'cursos/cursos.html')