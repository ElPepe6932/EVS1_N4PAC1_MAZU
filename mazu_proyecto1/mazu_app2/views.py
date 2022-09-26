from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.

def vistaApp2_fecha_hora(request):
    fh = datetime.datetime.now()
    p = "<br><h3>Fecha y hora</h3><hr><div><p>la fecha y la hora actual son :</p></div>"+str(fh)
    return HttpResponse(p)

def vistaApp2_Lista(request):
    pass
