from django.db.models.base import Model
from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from django import forms

from administrativo.models import Casa, \
        Departamento, Persona, Barrio





class CasaForm(ModelForm):
    class Meta:
        model = Casa
        fields = ['propietario_nombre',  'direccion', 'barrio', 
        'valor_bien', 'color_inmueble', 'num_cuarto', 'num_pisos']
        labels = {
            'propietario_nombre': _('Ingrese nombre por favor'),
            'direccion': _('Ingrese direccion por favor'),
            'barrio': _('Ingrese barrio por favor'),
            'valor_bien': _('Ingrese valor_bien por favor'),
            'color_inmueble': _('Ingrese color_inmueble por favor'),
            'num_cuarto': _('Ingrese num_cuarto por favor'),
            'num_pisos': _('Ingrese num_pisos por favor'),
        }




class DepartamentoForm(ModelForm):
    class Meta:
        model = Departamento
        fields = ['propietario_nombre', 'direccion', 'barrio', 'valor_bien',
        'num_cuarto', 'valor_mensual']
        labels = {
            'propietario_nombre': _('Ingrese nombre por favor'),
            'direccion': _('Ingrese direccion por favor'),
            'barrio': _('Ingrese barrio por favor'),
            'valor_bien': _('Ingrese costo total por favor'),
            'num_cuarto': _('Ingrese numero de cuartos por favor'),
            'valor_mensual': _('Ingrese costo mensual por favor'),
        }


class PersonaForm(ModelForm):
    class Meta:
        model = Persona
        fields = ['nombres', 'apellidos', 'cedula', 'correo']
        labels = {
            'nombres': _('Ingrese nombre por favor'),
            'apellidos': _('Ingrese direccion por favor'),
            'cedula': _('Ingrese barrio por favor'),
            'correo': _('Ingrese costo total por favor'),
        }

class BarrioForm(ModelForm):
    class Meta:
        model = Barrio
        fields = ['nombre_barrio', 'siglas']
        labels = {
            'nombre_barrio': _('Ingrese nombre por favor'),
            'siglas': _('Ingrese direccion por favor'),
        }