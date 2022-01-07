import pymysql

# items = [
#     ('bicicleta', 63),
#     ('laptop', 23),
#     ('audifonos', 12)
# ]

try:
    conexion = pymysql.connect(host='localhost',
                               user='root',
                               password='5303@Root$',
                               db='curso_flask')

    # cursor = conexion.cursor()

    # sql = "insert into curso (nombre, credito) values (%s,%s)"
    # cursor.executemany(sql, items)

    # conexion.commit()

    print("Conexión correcta")
except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
    print("Ocurrió un error al conectar: ", e)

finally:
    conexion.close()
