class Libro:

    __val_id = [
        (lambda x : type(x) == int, "No es del tipo correcto")
    ]
    __val_str = [
        (lambda x : type(x) == str, "No es del tipo correcto"),
        (lambda x: len(x.strip()) > 0, "No puede ser vacio")
    ]
    __val_precio = [
         (lambda x : type(x) == float, "No es del tipo correcto"),
         (lambda x : x > 0, "Tiene que ser mayor que cero")

    ]

    campos = {'id': __val_id, 'titulo': __val_str, 'anio_edicion': __val_str, 'precio': __val_precio}

    @staticmethod
    def json(id, titulo, anio_edicion, precio):
        return {'id': id, 'titulo': titulo, 'anio_edicion': anio_edicion, 'precio': precio}