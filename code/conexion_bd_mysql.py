import pymysql



class ConexionBdMySql:

    @staticmethod
    def obtener_conexion():
        return pymysql.connect(host='localhost',
                                    user='root',
                                    password='5303@Root$',
                                    db='curso_flask_2')

# Ejemplo de uso:
# dict1 = {'titulo': 'El retrato de Dorian', 'anio_edicion': '1990', 'precio': 68.32}
# Debajo de cada metodo lo que devuelve. Fue tomado como ejemplo dict1. Tambien funciona 
# con un listado de diccionarios. 

    @staticmethod
    def __met_helper(data):
        campos = None
        if type(data) == dict:
            campos = tuple(data)
        else:
            campos = tuple(data[0])
        return campos

    @staticmethod
    def get_campos(data):
        campos = ConexionBdMySql.__met_helper(data)
        stringP = ""
        for i in range(len(campos)):
            stringP += f"{campos[i]}, " if len(campos) - 1 != i else f"{campos[i]}"
        return stringP

    # Devuelve: titulo, anio_edicion, precio

    @staticmethod
    def get_caracteres(data):
        campos = ConexionBdMySql.__met_helper(data)
        caracteres = ""
        for i in range(len(campos)):
            caracteres += "%s, " if len(campos) - 1 != i else "%s"
        return caracteres

    # Devuelve: %s, %s, %s

    @staticmethod
    def get_valores(data):
        if type(data) == dict:
            return tuple(data.values())

        else:
            listaTemp = []
            for json in data:
                listaTemp.append(tuple(json.values()))
        return listaTemp

        # Devuelve: ('El retrato de Dorian', '1990', 68.32)