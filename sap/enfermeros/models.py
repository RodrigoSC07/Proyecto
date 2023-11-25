from django.db import models

# Create your models here.
class Enfermedad(models.Model):
    familiar = models.CharField(max_length=40, null=True)

    def __str__(self):
        return f'{self.familiar}'

class Datos(models.Model):
    diagnostico = models.CharField(max_length=20, null=True)
    peso = models.IntegerField(null=True)
    altura = models.DecimalField(max_digits=4, decimal_places=2, null=True)
    alergia = models.CharField(max_length=100, null=True)

    def __str__(self):
        return f'{self.diagnostico}'

class Enfermero(models.Model):
    GENERO = [
        ("M", "Masculino"),
        ("F", "Femenino"),
    ]

    cedula = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    genero = models.CharField(max_length=1, choices=GENERO, null=True)
    especialidad = models.CharField(max_length=20)
    celular = models.CharField(max_length=50)
    correo = models.CharField(max_length=50)
    dato = models.ForeignKey(Datos, on_delete=models.SET_NULL, null=True)
    antecedentes = models.ForeignKey(Enfermedad, on_delete=models.SET_NULL, null=True)
    activo = models.BooleanField(default=True)


