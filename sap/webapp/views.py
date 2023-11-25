from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from enfermeros.models import Enfermero

def bienvenida2(request):
    cantidad_enfermeros = Enfermero.objects.count()
    enfermeros = Enfermero.objects.all()
    enfermeros = Enfermero.objects.order_by('apellido', 'nombre')
    print(f'Cantidad enfermeros: {cantidad_enfermeros}')
    dict_datos = {'cantidad_enfermeros': cantidad_enfermeros, 'enfermeros': enfermeros}
    pagina = loader.get_template('bienvenida.html')
    return HttpResponse(pagina.render(dict_datos, request))
