from typing import Dict

class Validacion:
    @staticmethod
    def validar(modelo: Dict, json: Dict, metodo = "POST"):
        if metodo == 'POST':
            llaves = [llave for llave in list(modelo) if llave != 'id']
        else:
            llaves = list(modelo)
        for llave in llaves:
            if json.get(llave) == None and modelo[llave][1] == True:
                raise ValueError(f"{llave} => Campo obligatorio.")
            if modelo[llave][0] != None:
                for func in modelo[llave][0]:
                    if json.get(llave) != None:
                        if not func[0](json[llave]):
                            raise ValueError(f"'{llave}' => {func[1]}")