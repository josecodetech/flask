from flask import Flask, redirect, request, url_for, render_template, flash, session
from werkzeug.security import check_password_hash as checkph
from werkzeug.security import generate_password_hash as genph

import basedatos

app = Flask(__name__)
app.secret_key = 'miclavesecreta'


@app.before_request
def antes_de_todo():
    ruta = request.path
    if not 'usuario' in session and ruta != "/entrar" and ruta != "/login" and ruta != "/salir" and ruta != "/registro":
        flash("Inicia sesion para continuar")
        return redirect("/entrar")


@app.route("/dentro")
def dentro():
    return render_template("index.html")


@app.route("/")
@app.route("/entrar")
def entrar():
    return render_template("entrar.html")


@app.route("/login", methods=["POST"])
def login():

    email = request.form['email']
    contraseña = request.form['contraseña']
    try:
        usuario = basedatos.obtener_usuario(email)
    except Exception as e:
        flash("Error al obtener usuario")
    if usuario:
        if(checkph(usuario[1], contraseña)):
            session['usuario'] = email
            return redirect("/dentro")
        else:
            flash("Acceso denegado")
            return redirect("/entrar")

    return redirect("/entrar")


@app.route("/salir")
def salir():
    session.pop("usuario", None)
    flash("Sesion cerrada")
    return redirect("/entrar")


@app.route("/registro")
def registro():
    return render_template("registro.html")


@app.route("/registrar", methods=['POST'])
def registrar():
    email = request.form['email']
    contraseña = request.form['contraseña']
    contraseña = genph(contraseña)

    try:
        basedatos.alta_usuario(email, contraseña)
        flash("usuario registrado")

    except Exception as e:
        flash("error al registrar usuario")
    finally:

        return redirect("/entrar")


if __name__ == '__main__':
    app.run(debug=True)
