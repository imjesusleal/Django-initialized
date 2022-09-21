from django.http import HttpResponse
from django.shortcuts import render
from .models import Directores

def index(request):
    directores_lista = Directores.objects.all()
    context = {
        'directores_lista': directores_lista,
    }
    return render(request, 'Components/index.html', context)

def directores(request, Directores_id):
    return HttpResponse(Directores_id)
    


def peliculas (request, Peliculas_id):
    return HttpResponse(Peliculas_id)    

# Create your views here.
