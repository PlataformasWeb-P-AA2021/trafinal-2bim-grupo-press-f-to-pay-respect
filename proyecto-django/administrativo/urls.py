"""
    Manejo de urls para la aplicación
    administrativo
"""
from django.urls import path
# se importa las vistas de la aplicación
from . import views


urlpatterns = [
        path('', views.index, name='index'),
        path('casas/', views.casa, name="casa"),
        path('departamentos/', views.departamentos, name="departamentos"),
        path('casa/crear/', views.crear_casa, name="crear_casa"),
        path('departamentos/crear/', views.crear_departamento, name="crear_departamento"),
        path('persona/crear/', views.crear_persona, name="crear_persona"),
        path('barrio/crear/', views.crear_barrio, name="crear_barrio"),
        path('eliminar/casa/<int:id>', views.eliminar_casa,name='eliminar_casa'),
        path('eliminar/departamento/<int:id>', views.eliminar_departamento,name='eliminar_departamento'),
        path('editar_casa/<int:id>', views.editar_casa,
            name='editar_casa'),
        path('editar_departamento/<int:id>', views.editar_departamento,
            name='editar_departamento'),

        path('saliendo/logout/', views.logout_view, name="logout_view"),
        path('entrando/login/', views.ingreso, name="login"),
        
 ]
