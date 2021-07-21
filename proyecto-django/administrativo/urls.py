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
        path('saliendo/logout/', views.logout_view, name="logout_view"),
        path('entrando/login/', views.ingreso, name="login"),
        
 ]
