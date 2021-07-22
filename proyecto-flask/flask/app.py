from flask import Flask, render_template
import requests
import json

app = Flask(__name__, template_folder='templates')

@app.route("/")
def hello_world():
    return "<p>Hello, Ricardo!</p>"


@app.route("/departamento")
def los_departamentos():
    """
    """
    r = requests.get("http://127.0.0.1:8000/api/departamento/",
            auth=('admin', '123'))
    departamento = json.loads(r.content)['results']
    numero_Departamentos = json.loads(r.content)['count']
    return render_template("departamento.html", departamento=departamento,
    numero_Departamentos=numero_Departamentos)


@app.route("/casa")
def las_casas():
    """
    """
    r = requests.get("http://127.0.0.1:8000/api/casa/",
            auth=('admin', '123'))
    datos = json.loads(r.content)['results']
    numero = json.loads(r.content)['count']
    return render_template("casas.html", datos=datos,
    numero=numero)

@app.route("/personas")
def personas():
    """
    """
    r = requests.get("http://127.0.0.1:8000/api/persona/",
            auth=('admin', '123'))
    datos = json.loads(r.content)['results']
    numero = json.loads(r.content)['count']
    return render_template("personas.html", datos=datos,
    numero=numero)

@app.route("/barrio")
def barrio():
    """
    """
    r = requests.get("http://127.0.0.1:8000/api/barrio/",
            auth=('admin', '123'))
    datos = json.loads(r.content)['results']
    numero = json.loads(r.content)['count']
    return render_template("barrio.html", datos=datos,
    numero=numero)

######################################################
@app.route("/personasdasda")
def dasda():
    """
    """
    r = requests.get("http://127.0.0.1:8000/api/numerost/",
            auth=('dani', '123'))
    datos = json.loads(r.content)['results']
    numero = json.loads(r.content)['count']
    datos2 = []
    for d in datos:
        datos2.append({'telefono':d['telefono'], 'tipo':d['tipo'],
        'estudiante': dasda(d['estudiante'])})
    return render_template("lostelefonosdos.html", datos=datos2,
    numero=numero)

# funciones ayuda

def dasda(url):
    """
    """
    r = requests.get(url, auth=('dani', '123'))
    nombre_estudiante = json.loads(r.content)['nombre']
    return nombre_estudiante
