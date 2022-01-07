import pymysql


def obtener_conexion():
    return pymysql.connect(host='localhost',
                                user='root',
                                password='5303@Root$',
                                db='curso_flask_2')
