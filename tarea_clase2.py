from flask import Flask, request, jsonify

app = Flask(__name__)
@app.route ('/')
def index():
    return"<h3>Un saludo personalizado</h3>"
@app.route('/mensaje/<nombre>/<apellido>', methods=['GET'])
@app.route('/mensaje/<nombre>', methods=['GET'])
@app.route('/mensaje/', methods=['GET'])
	@@ -25,12 +24,11 @@ def mensaje_saludo_2(nombre=None, apellido=None):
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
	@@ -93,12 +91,12 @@ def lista_materias(ciclo=None):
    cadena = """<h3>Lista de Materias del ciclo %s</h3><ul>""" % (ciclo)

    for i in lista:
        cadena = """%s
        <li>
        %s
        </li> """ %(cadena, i)
        mensaje = "%s</ul>" % (cadena)
    return f"""{mensaje}"""

if __name__ == "__main__":
    app.run(threaded=True, port=5000)
