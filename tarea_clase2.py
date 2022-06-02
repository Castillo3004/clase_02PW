from flask import Flask, request, jsonify

app = Flask(__name__)
@app.route ('/')
def index():
    return"<h3>Un saludo personalizado</h3>"
@app.route('/mensaje/<nombre>/<apellido>', methods=['GET'])
@app.route('/mensaje/<nombre>', methods=['GET'])
@app.route('/mensaje/', methods=['GET'])
def mensaje_saludo(nombre=None, apellido=None):
    response = {}
    if not nombre or not apellido:
        response["ERROR"] = "Datos faltantes para presenta mensaje"
    else:
        response["MESSAGE"] = f"Hola {nombre} {apellido} bienvenido a la plataforma"
    # Return the response in json format
    return jsonify(response)
@app.route('/mensaje/2/<nombre>/<apellido>', methods=['GET'])
@app.route('/mensaje/2/', methods=['GET'])
def mensaje_saludo_2(nombre=None, apellido=None):
    response = {}
    if not nombre or not apellido:
        response["ERROR"] = "no name found, please send a name."
        return """<h3>Error: {response['ERROR']} </h3>"""
    else:
        response["MESSAGE"] = f"Hola {nombre} {apellido} bienvenido a la plataforma"
    # Return the response in json format
        return f"""<h3>{response['MESSAGE']}</h3>"""
@app.route('/materias/<ciclo>/', methods=['GET'])
def lista_materias(ciclo=None):
    """
    """

    diccionario = {'1': ["Fundamentos Computacionales",
"Fundamentos Matemáticos",
"Humanismo, Universidad y Cultura",
"Introducción a la Programación",
"Computación y Sociedad",
"Estructuras Discretas"],
'2':["Física Básica",
"Álgebra  Lineal",
"Análisis Matemático Univariado",
"Estructuras de datos",
"Programación Orientada a Objetos"],
'3':["Ecuaciones Diferenciales y Métodos Numéricos",
"Lógica Digital",
"Fundamentos de Base de Datos",
"Programación Funcional y Reactiva",
"Antropología Básica",
"Prácticum 1.1"],
'4':["Arquitectura y Organización de Computadores",
"Análisis de Algoritmos",
"Base de Datos Avanzada",
"Programación Avanzada",
"Prototipado",
"Prácticum 1.2"],
'5':["Sistemas Operativos",
"Introducción a la Inteligencia de Negocios",
"Ingeniería Web",
"Estadística y Probabilidad",
"Ética y Moral",
"Fundamentos de Ingeniería de Software",
"Prácticum 2.1"],
'6':["Teoría de Autómatas y  Compiladores",
"Fundamentos de Redes",
"Ingeniería de Requisitos",
"Gestión de la calidad de software",
"Itinerario I: Plataformas Web",
"Itinerario II: Fundamentos de Análisis de Datos",
"Prácticum 2.2"],
'7':["Redes y Sistemas Distribuidos",
"Fundamentos de Inteligencia Artificial",
"Arquitectura de Software",
"Emprendimiento",
"Itinerario I: Plataformas Móviles",
"Itinerario II: Interoperabilidad y Explotación de Datos en Ecosistemas Heterogéneos",
"Prácticum 3. Servicio Comunitario"],
'8':["Computación Paralela y Distribuida",
"Representación Avanzada del Conocimiento y Razonamiento",
"Emprendimiento de Base Tecnológica I",
"Composición de Textos Científicos",
"Prácticum 4.1",
"Itinerario I: Plataformas para Juegos",
"Itinerario II: Análisis y Visualización de Grandes Volúmenes de Datos"],
'9':["Gestión de Proyectos",
"Seguridad de la Información",
"Tecnologías Emergentes",
"Emprendimiento de Base Tecnológica II",
"Sistemas Inteligentes",
"Prácticum 4.2"]
}
    lista = diccionario[ciclo]
    cadena = """<h3>Lista de Materias del ciclo %s</h3><ul>""" % (ciclo)
    
    for i in lista:
        cadena = """%s
        <li>
        %s
        </li> """ %(cadena, i)
        mensaje = "%s</ul>" % (cadena)
    return f"""{mensaje}"""

if __name__ == "__main__":
    app.run(debug=True)