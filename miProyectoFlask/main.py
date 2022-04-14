from flask import Flask, redirect, url_for, render_template
# creamos instancia de Flask
app = Flask(__name__)


@app.route('/')
def index():
    #encabezado = "Encabezado desde flask"
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
    return render_template('acercade.html')


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


if __name__ == '__main__':
    app.run(debug=True, port=5000)
