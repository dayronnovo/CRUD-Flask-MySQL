import pymysql
try:
    conexion = pymysql.connect(host='localhost',
                               user='root',
                               password='5303@Root$',
                               db='curso_flask_2')
    print("Conexión correcta")
except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
    print("Ocurrió un error al conectar: ", e)
