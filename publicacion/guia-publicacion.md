<h2> Guinicorn </h2>

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
5 - Levantamos el proyecto en gunicorn con: gunicorn <code> --bind 0.0.0.0:8000 nombre.wsgi </code>

---Aqui se termina la parte de Guinicorn---

<h2> Nginx </h2>

6 - En el directorio /etc/systemd/system/ agregar un archivo con la siguiente extension "nombre.service" esto debe ser con sudo, colocamos lo siguiente
 <pre>
 [Unit]
# metadatos necesarios
Description=gunicorn daemon
After=network.target

[Service]
# usuario del sistema operativo que ejecutará el proceso
User=usuario-sistema-operativo
# el grupo del sistema operativo que permite la comunicación a desde el servidor web-nginx con gunicorn. No se debe cambiar el valor
Group=www-data

# a través de la variable WorkingDirectory se indica la dirección absoluta del proyecto de Django
WorkingDirectory=/home/usuario-sistema/carpeta/proyectos/nombre-proyecto

# En Environment se indica el path de python
# Ejemplo 1: /usr/bin/python3.9
# Ejemplo 2: (Opcional, con el uso de entornos virtuales) /home/usuario/entornos/entorno01/bin
Environment="PATH=agregar-path-python"

# Detallar el comando para iniciar el servicio
ExecStart=path-python/bin/gunicorn --workers 3 --bind unix:application.sock -m 007 proyectoDjango.wsgi:application

# Donde: aplicacion.sock es el nombre del archivo que se debe crear en el directorio del proyecto; proyectoDjango el nombre del proyecto que se intenta vincular con nginx.
# La expresión /bin/gunicorn no se debe modificar.

[Install]
# esta sección será usada para indicar que el servicio puede empezar cuando se inicie el sistema operativo. Se sugiere no cambiar el valor dado.
WantedBy=multi-user.target
 
 </pre>
7 - Iniciar y habilitar el proceso mediante los siguientes comandos
<pre>
<code>  sudo systemctl start nombre </code>
<code>  sudo systemctl enable nombre </code>
</pre>
8 - Verificar que todo este correcto mediante con: <code> sudo systemctl status nombre </code>

9 - Iniciamos con los comandos para el servicio:
<pre>
  <code> sudo service nginx start</code>
  <code> sudo service nginx stop</code>
  <code> sudo service nginx restart</code>
  <code> sudo service nginx statu</code>
</pre>
10 - Crear el archivo sites-available de nginx, con sudo ejemplo de ruta "/etc/nginx/sites-available", con la siguiente estructura
<pre>
server {
    listen 81;
    server_name localhost;
    
    location / {
        include proxy_params;
        proxy_pass http://unix:/ruta/al/archivo/sock/application.sock;
    }

    
    location /static/ {
        root /ruta/a/la/carpeta/staticos/del/proyecto-django;
    }

}
</pre>

11 - Creamos con sudo touch /etc/nginx/sites-available/nombre

12 - Iniciar un enlace simbólico del archivo creado en el directorio sites-available.
<code> sudo ln -s /etc/nginx/sites-available/proyecto01 /etc/nginx/sites-enabled </code>

13 - Iniciar el serivicio, si no se tiene ningun error debe aparecer en "0.0.0.0:81"
