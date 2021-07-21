from django.contrib import admin

# Register your models here.
from administrativo.models import Casa, Departamento, Persona, Barrio

class PersonaAdmin(admin.ModelAdmin):

    list_display = ('nombres', 'apellidos', 'cedula', 'correo')

    search_fields = ('nombres', 'apellidos')
    
admin.site.register(Persona, PersonaAdmin)


class BarrioAdmin(admin.ModelAdmin):

    list_display = ('nombre_barrio', 'siglas')

    search_fields = ('nombre_barrio', 'siglas')
    
admin.site.register(Barrio, BarrioAdmin)

class CasaAdmin(admin.ModelAdmin):

    list_display = ('propietario_nombre', 'direccion', 'barrio', 'valor_bien', 'color_inmueble', 'num_cuarto', 'num_pisos')
    search_fields = ('propietario_nombre', 'direccion')

admin.site.register(Casa, CasaAdmin)


class DepartamentoAdmin(admin.ModelAdmin):
 
    list_display = ('propietario_nombre', 'direccion', 'barrio', 'valor_bien', 'num_cuarto', 'valor_mensual')

    search_fields = ('propietario_nombre', 'direccion')
    
admin.site.register(Departamento, DepartamentoAdmin)


