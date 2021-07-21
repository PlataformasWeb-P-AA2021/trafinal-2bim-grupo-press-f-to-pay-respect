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
        path('departamentoscrear/', views.crear_departamento, name="crear_departamento"),
        path('saliendo/logout/', views.logout_view, name="logout_view"),
        path('entrando/login/', views.ingreso, name="login"),
        
 ]
