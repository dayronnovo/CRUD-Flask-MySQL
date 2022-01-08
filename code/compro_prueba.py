class Validacion:
    @staticmethod
    def add_argument(data, campo, tipo, requerido):
        if requerido == True:
            if data.get(campo) == None:
                raise ValueError(f"El campo: '{campo}' es obligatorio")
        if type(data[campo]) != tipo:
            raise TypeError(f"El campo: '{campo}' no es del tipo correcto")
