import pymysql


def dame_conexion():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='',
        db='basedatosflask'
    )


def alta_usuario(email, clave):
    conexion = dame_conexion()
    with conexion.cursor() as cursor:
        cursor.execute(
            "INSERT INTO usuarios(email,clave) VALUES (%s,%s)", (email, clave)
        )

        conexion.commit()
        conexion.close()


def obtener_usuario(email):
    conexion = dame_conexion()
    usuario = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT email, clave FROM usuarios WHERE email=%s", (email)
        )
        usuario = cursor.fetchone()
        conexion.close()
        return usuario


if __name__ == '__main__':
    alta_usuario('jdkjf@gmail.com', 'jkadjfj2j42kjk2j')
    print(obtener_usuario('jdkjf@gmail.com')[1])
