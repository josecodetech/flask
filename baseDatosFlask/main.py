import re
from flask import Flask, redirect, request, url_for, render_template
import basedatos
app = Flask(__name__)


@app.route('/agregar_articulo')
def agregar_articulo():
    return render_template("agregar_articulo.html")


@app.route('/guardar_articulo', methods=['POST'])
def guardar_articulo():
    nombre = request.form['nombre']
    precio = request.form['precio']
    try:
        basedatos.insertar_articulo(nombre, precio)
    except Exception as e:
        print(f"Ha ocurrido el error {e}")
    finally:
        return redirect('/articulos')


@ app.route('/')
@ app.route('/articulos')
def articulos():
    try:
        articulos = basedatos.listar_articulos()
    except Exception as e:
        print(f"Ha ocurrido el error {e}")
    finally:
        return render_template('articulos.html', articulos=articulos)


@ app.route("/eliminar_articulo", methods=['POST'])
def eliminar_articulo():
    try:
        basedatos.eliminar_articulo(request.form['id'])
    except Exception as e:
        print(f"Ha ocurrido el error {e}")
    finally:

        return redirect("/articulos")


@ app.route("/editar_articulo/<int:id>")
def editar_articulo(id):
    try:
        articulo = basedatos.obtener_articulo(id)
    except Exception as e:
        print(f"Ha ocurrido el error {e}")
    finally:
        return render_template("editar_articulo.html", articulo=articulo)


@ app.route("/actualizar_articulo", methods=['POST'])
def actualizar_articulo():
    id = request.form["id"]
    nombre = request.form["nombre"]
    precio = request.form["precio"]
    try:
        basedatos.actualizar_articulo(id, nombre, precio)
    except Exception as e:
        print(f"Ha ocurrido el error {e}")
    finally:
        return redirect("/articulos")


if __name__ == '__main__':

    app.run(debug=True)
