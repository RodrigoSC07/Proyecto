from django.forms import ModelForm, EmailInput

from enfermeros.models import Enfermero

class EnfermeroFormulario(ModelForm):
    class Cura:
        model = Enfermero
        fields = ('cedula', 'nombre', 'apellido', 'genero', 'especialidad', 'celular', 'correo' 'dato', 'activo',)
        widgets = {
            'correo': EmailInput(attrs={'type': 'correo'})
        }
