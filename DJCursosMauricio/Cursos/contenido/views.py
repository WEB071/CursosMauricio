from django.http import HttpRequest
from django.shortcuts import render, HttpResponse

# Create your views here.


# Vistas
def principal(request):
    return render(request, 'inicio/principal.html')
  
def contacto(request):
    return render(request, 'inicio/contacto.html')
  
def cursos(request):
    return render(request, 'inicio/cursos.html')
  
  