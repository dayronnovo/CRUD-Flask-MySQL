import pymysql



class ConexionBdMySql:

    @staticmethod
    def obtener_conexion():
        return pymysql.connect(host='localhost',
                                    user='root',
                                    password='5303@Root$',
                                    db='curso_flask_2')
    @staticmethod
    def get_campos(data):
        campos = None
        if type(data) == dict:
            campos = tuple(data)
        else:
            campos = tuple(data[0])
        stringP = ""
        for i in range(len(campos)):
            stringP += f"{campos[i]}, " if len(campos) - 1 != i else f"{campos[i]}"
        return stringP

    @staticmethod
    def get_caracteres(data):
        campos = None
        if type(data) == dict:
            campos = tuple(data)
        else:
            campos = tuple(data[0])
        caracteres = ""
        for i in range(len(campos)):
            caracteres += f"{'%s , '}" if len(campos) - 1 != i else "%s"
        return caracteres



    @staticmethod
    def get_valores(data):
        if type(data) == dict:
            return tuple(data.values())

        if type(data) == list:
            listaTemp = []
            for json in data:
                listaTemp.append(tuple(json.values()))
        return listaTemp