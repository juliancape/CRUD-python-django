from django.shortcuts import render, redirect
from .models import Curso
from django.contrib import messages

# Create your views here.

def home(request): 
    cursos_listados = Curso.objects.all()
    messages.success(request, '!Cursos Listados!')
    return render(request, 'gestionCursos.html', {'cursos': cursos_listados})

def registrarCurso(request):
    codigo_nuevo = request.POST['txtCodigo']
    nombre_nuevo = request.POST['txtNombre']
    creditos_nuevo = request.POST['numCreditos']

    curso = Curso.objects.create(codigo = codigo_nuevo, nombre= nombre_nuevo, creditos = creditos_nuevo)
    messages.success(request, '!Curso Registrado!')
    return redirect('/')

def editarCurso(request, codigo):
    curso = Curso.objects.get(codigo = codigo)
    return render(request, 'editarCurso.html', {'curso': curso})

def edicionCurso(request):
    codigo_nuevo = request.POST['txtCodigo']
    nombre_nuevo = request.POST['txtNombre']
    creditos_nuevo = request.POST['numCreditos']
    curso = Curso.objects.get(codigo = codigo_nuevo)
    curso.nombre = nombre_nuevo
    curso.creditos = creditos_nuevo
    curso.save()
    messages.success(request, '!Curso Editado!')
    return redirect('/')


def eliminarCurso(request, codigo):
    curso = Curso.objects.get(codigo = codigo)
    curso.delete()
    messages.success(request, '!Curso Eliminado!')

    return redirect('/')