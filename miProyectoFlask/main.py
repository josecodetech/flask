from flask import Flask
# creamos instancia de Flask
app = Flask(__name__)


@app.route('/')
def index():
    return "Texto cambiado sobre la marcha232323232323"


@app.route('/acercade')
def acercade():
    return "<h1>Acerca de mi</h1>"
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
