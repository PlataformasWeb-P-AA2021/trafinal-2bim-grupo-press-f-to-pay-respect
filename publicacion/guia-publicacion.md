<h2> Guinicorn

1 - Instalar la libreria gunicorn "get apt install gunicorn"

2 - Agregar la variable ALLOWED_HOSTS en el archivo settings.py para permitir el acceso a gunicorn desde el servidor web ALLOWED_HOSTS = ["0.0.0.0", "127.0.0.1"]

3 - Agregar en el archivo urls.py lo siguiente

  importamos:
<pre>
  from django.contrib.staticfiles.urls import staticfiles_urlpatterns

  agregamos en urlpatterns, despues []
  
  urlpatterns += staticfiles_urlpatterns()
</pre>
4 - Recopilar el contenido de la carpeta mediante la linea:   <code> python manage.py collectstatic  </code>
5 - Levantamos el proyecto en gunicorn con: gunicorn <code> --bind 0.0.0.0:8000 trabajoFinal.wsgi </code>

---Aqui se termina la parte de Guinicorn---

6 - En el directorio /etc/systemd/system/ agregar un archivo con la siguiente extension "nombre.service" esto debe ser con sudo
7 - Iniciar y habilitar el proceso mediante los siguientes comandos
<pre>
<code>  sudo systemctl start nombre </code>
<code>  sudo systemctl enable nombre </code>
</pre>
8 - Verificar que todo este correcto mediante cono: sudo systemctl status nombre

9 - Iniciamos con los comandos para el servicio:
<pre>
  <code> sudo service nginx start</code>
  <code> sudo service nginx stop</code>
  <code> sudo service nginx restart</code>
  <code> sudo service nginx statu</code>
</pre>
10 - Crear el archivo sites-available de nginx, con sudo ejemplo de ruta "/etc/nginx/sites-available"
11 - Creamos con sudo touch /etc/nginx/sites-available/nombre

12 - Iniciar un enlace simbólico del archivo creado en el directorio sites-available.
sudo ln -s /etc/nginx/sites-available/proyecto01 /etc/nginx/sites-enabled

13 - Iniciar el serivicio, si no se tiene ningun error debe aparecer en "0.0.0.0:81"
