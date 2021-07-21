from django.db import models
from django.db.models.fields import CharField

# Create your models here.

class Persona(models.Model):
    nombres = models.CharField(max_length=60)
    apellidos = models.CharField(max_length=60)
    cedula = models.CharField(max_length=15)
    correo = models.EmailField(max_length=60)

    

    def __str__(self):
        return "%s %s %s %s" % (self.nombres,
                self.apellidos,
                self.cedula,
                self.correo)        

class Barrio(models.Model):
    nombre_barrio = models.CharField(max_length=60)
    siglas = models.CharField(max_length=10)


    def __str__(self):
        return "%s %s %s %s" % (self.nombre_barrio,
                self.siglas)  


class Casa(models.Model):
    propietario_nombre = models.ForeignKey(Persona, on_delete=models.CASCADE, related_name="personacasa")
    direccion = models.CharField(max_length=60)
    barrio = models.ForeignKey(Barrio, on_delete=models.CASCADE, related_name="barrioscasa")
    valor_bien = models.IntegerField()
    color_inmueble = models.CharField(max_length=20)
    num_cuarto = models.IntegerField()
    num_pisos = models.IntegerField()


    def __str__(self):
        return "%s %s %s %d %s %d %d" % (self.propietario_nombre,
                self.direccion,
                self.barrio,
                self.valor_bien,
                self.color_inmueble,
                self.num_cuarto,
                self.num_pisos)

class Departamento(models.Model):
    propietario_nombre = models.ForeignKey(Persona, on_delete=models.CASCADE, related_name="personadepartamento")
    direccion = models.CharField(max_length=60)
    barrio = models.ForeignKey(Barrio, on_delete=models.CASCADE, related_name="barriodepa")
    valor_bien = models.IntegerField()
    num_cuarto = models.IntegerField()
    valor_mensual = models.IntegerField()

    def __str__(self):
        return "%s %s %s %d %d %d" % (self.propietario_nombre,
                self.direccion,
                self.barrio,
                self.valor_bien,
                self.num_cuartos,
                self.valor_mensual)
