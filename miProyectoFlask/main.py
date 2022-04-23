from flask import Flask, redirect, url_for, render_template, request
# creamos instancia de Flask
app = Flask(__name__)


@app.before_request
def before_request():
    print("Antes de la peticion")


@app.after_request
def after_request(response):
    print("Despues de la peticion")
    return response


@app.route('/')
def index():
    #encabezado = "Encabezado desde flask"
    print("Accediendo al index o pagina principal")
    diccionario = {'titulo': 'Pagina principal',
                   'encabezado': 'Bienvenido a mi pagina web'}
    return render_template('index.html', datos=diccionario)
    # return "Estamos en INDEX o pagina principal"


@app.route('/redirecciona')
@app.route('/redirecciona/<string:sitio>')
def redirecciona(sitio=None):
    if sitio is not None:
        return redirect(url_for('index'))
    else:
        return redirect(url_for('acercade'))


@app.route('/acercade')
def acercade():
    # return "<h1>Acerca de mi</h1>"
    diccionario = {'titulo': 'Acerca de',
                   'encabezado': 'Acerca de mi'}
    return render_template('acercade.html', datos=diccionario)


@app.route('/condicionybucle')
def condicionybucle():

    datos = {
        'edad': 50,
        'nombres': ['Jose', 'Mar', 'Lucia', 'Eva']
    }
    return render_template('condicionybucle.html', datos=datos)

# Con parametros


@app.route('/saludame')
@app.route('/saludame/<string:nombre>')
@app.route('/saludame/<string:nombre>/<int:edad>')
def saludame(nombre='Jose', edad=None):
    if edad != None:
        return "Hola {} tienes {} años".format(nombre, edad)
    else:
        return f""" 
            <h1>Hola, </h1>
            <h3>{nombre}</h3>
            
        
"""


@app.route('/suma/<int:num1>/<int:num2>')
def suma(num1, num2):
    suma = num1 + num2
    return f""" La suma es igual a {suma}"""


def pagina_no_encontrada(error):
    return render_template('errores/404.html'), 404


if __name__ == '__main__':
    app.register_error_handler(404, pagina_no_encontrada)
    app.run(debug=True, port=5000)
