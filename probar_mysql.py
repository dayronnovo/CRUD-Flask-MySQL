import pymysql

# items = [
#     ('bicicleta', 63),
#     ('laptop', 23),
#     ('audifonos', 12)
# ]
dict1 = {'titulo': 'El retrato de Dorian', 'anio_edicion': '1990', 'precio': 68.32}
dict2 = [{'titulo': 'El retrato de Dorian', 'anio_edicion': '1990', 'precio': 68.32}, {'titulo': 'El retrato de Dorian', 'anio_edicion': '1990', 'precio': 68.32}, {'titulo': 'El retrato de Dorian', 'anio_edicion': '1990', 'precio': 68.32}]

campos = tuple(dict1)
stringP = ""
for i in range(len(campos)):
    stringP += f"{campos[i]}, " if len(campos) - 1 != i else f"{campos[i]}"
# print(f"Valores: {stringP}")


valores = tuple(dict1.values())
print(valores)

caracteres = ""
for i in range(len(campos)):
    caracteres += f"{'%s , '}" if len(campos) - 1 != i else "%s"
print(caracteres)

try:
    conexion = pymysql.connect(host='localhost',
                               user='root',
                               password='5303@Root$',
                               db='curso_flask_2')

    cursor = conexion.cursor()

    sql = f"insert into libros ({stringP}) values ({caracteres})"
    cursor.execute(sql, valores)

    conexion.commit()

    print("Conexión correcta")
except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
    print("Ocurrió un error al conectar: ", e)

finally:
    conexion.close()




# ================================================================
#              Como tenia el create en LibroService
# ================================================================

# @staticmethod
#     def create(item):  
#         conexion = ConexionBdMySql.obtener_conexion()
#         cursor = conexion.cursor()

#         print(item)

#         sql = f"insert into {LibroService.TABLE_NAME} ({ConexionBdMySql.get_campos(item)}) values ({ConexionBdMySql.get_caracteres(item)})"

#         if type(item) == dict:
#             cursor.execute(sql, ConexionBdMySql.get_valores(item))
#         else:
#             cursor.executemany(sql, ConexionBdMySql.get_valores(item))

#         conexion.commit()
#         conexion.close()