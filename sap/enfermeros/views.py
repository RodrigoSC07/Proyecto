from django.forms import modelform_factory
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template import loader

from enfermeros.forms import EnfermeroFormulario
from enfermeros.models import Enfermero

# Create your views here.

EnfermeroFormulario = modelform_factory(Enfermero, exclude=['activo',])

def agregar_enfermero(request):
    pagina = loader.get_template('agregar.html')
    if request.method == 'GET':
        formulario = EnfermeroFormulario
    elif request.method == 'POST':
        formulario = EnfermeroFormulario(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('inicio')
    datos = {'formulario': formulario}
    return HttpResponse(pagina.render(datos, request))

def modificar_enfermero(request, id):
    pagina = loader.get_template('modificar.html')
    enfermero = get_object_or_404(Enfermero, pk=id)
    if request.method == 'GET':
        formulario = EnfermeroFormulario(instance=enfermero)
    elif request.method == 'POST':
        formulario = EnfermeroFormulario(request.POST, instance=enfermero)
        if formulario.is_valid():
            formulario.save()
            return redirect('inicio')
    datos = {'formulario': formulario}
    return HttpResponse(pagina.render(datos, request))

def ver_enfermero(request, id):
    enfermero = Enfermero.objects.get(pk=id)
    enfermero = get_object_or_404(Enfermero, pk=id)
    datos = {'enfermero': enfermero}
    print(enfermero)
    pagina = loader.get_template('ver.html')
    return HttpResponse(pagina.render(datos, request))

def eliminar_enfermero(request, id):
    enfermero = get_object_or_404(Enfermero, pk=id)
    if enfermero:
        enfermero.delete()
        return redirect('inicio')
