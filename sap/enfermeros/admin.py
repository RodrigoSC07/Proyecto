from django.contrib import admin

from enfermeros.models import Enfermero, Datos, Enfermedad

# Register your models here.
admin.site.register(Enfermero)
admin.site.register(Datos)
admin.site.register(Enfermedad)
