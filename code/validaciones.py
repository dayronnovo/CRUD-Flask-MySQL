class Validacion:
    @staticmethod
    def validar(modelo, json, metodo = "POST"):
        if metodo == 'POST':
            llaves = [llave for llave in list(modelo) if llave != 'id']
        else:
            llaves = list(modelo)
        for llave in llaves:
            # print(modelo[llave])
            for func in modelo[llave]:
                try:
                    if not func[0](json[llave]):
                        raise ValueError(f"'{llave}' => {func[1]}")
                    # print(f"'{llave}' => {func[1]}")
                except KeyError as error:
                    raise ValueError(f"{error} => Campo obligatorio.")