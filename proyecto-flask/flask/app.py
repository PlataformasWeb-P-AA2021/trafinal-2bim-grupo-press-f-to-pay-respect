from flask import Flask, render_template
import requests
import json

app = Flask(__name__, template_folder='templates')

@app.route("/")
def hello_world():
    return "<p>Bienvenido al Municipio</p>"\
    "<BR><a href='/departamento'>Ver Departamentos</a>"\
    "<BR><a href='/casa'>Ver Casas</a>"\
    "<BR><a href='/personas'>Ver Personas</a>"\
    "<BR><a href='/barrio'>Ver Barrios</a>"\


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
@app.route("/departamento")
def los_departamentos():
    """
    """
    r = requests.get("http://127.0.0.1:8000/api/departamento/",
            auth=('admin', '123'))
    departamentox = json.loads(r.content)['results']
    numero_Departamentos = json.loads(r.content)['count']
    departamento = []
    for d in departamentox:
        departamento.append({'propietario_nombre': ObtPropietario(d['propietario_nombre']),
        'direccion':d['direccion'],
        'barrio': ObtNombreBarrio(d['barrio']),
         'valor_bien':d['valor_bien'],
         'num_cuarto':d['num_cuarto'],
         'valor_mensual':d['valor_mensual']
        })
    return render_template("departamento.html", departamento=departamento,
    numero_Departamentos=numero_Departamentos)


@app.route("/casa")
def las_casas():
    """
    """
    r = requests.get("http://127.0.0.1:8000/api/casa/",
            auth=('admin', '123'))
    datosx = json.loads(r.content)['results']
    numero = json.loads(r.content)['count']
    datos = []
    for d in datosx:
        datos.append({'propietario_nombre': ObtPropietario(d['propietario_nombre']),
        'direccion':d['direccion'],
        'barrio': ObtNombreBarrio(d['barrio']),
         'num_cuarto':d['num_cuarto'],
         'num_pisos':d['num_pisos'],
         'color_inmueble':d['color_inmueble'],
         'valor_bien':d['valor_bien']
        })
    return render_template("casas.html", datos=datos,
    numero=numero)

# funciones ayuda

def ObtPropietario(url):
    """
    """
    r = requests.get(url, auth=('admin', '123'))
    nombre_propietario = ("%s %s" % (json.loads(r.content)['nombres'], json.loads(r.content)['apellidos']))
    return nombre_propietario

def ObtNombreBarrio(url):
    """
    """
    r = requests.get(url, auth=('admin', '123'))
    nombre_Barrio = json.loads(r.content)['nombre_barrio']
    return nombre_Barrio