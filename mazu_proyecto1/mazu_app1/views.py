from urllib import request
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def vistaUno(request):
    s = "<h1>Hola a la Evaluacion 1</h1><br><hr><p>hablar hablar hablar</p><button>Inicio</button>"
    return HttpResponse(s)

def tablaUno(request):
    tabla = "<h2>Tabla para Evaluacion</h2><table border=solid><tr><th>Indice uno</th></tr><td>Dato uno</td></table>"
    return HttpResponse(tabla)