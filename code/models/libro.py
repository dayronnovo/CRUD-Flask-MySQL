# from autor import Autor


class Libro:
    def __init__(self, id, titulo, anio_edicion, precio, autor) -> None:
        self.id = id
        self.titulo = titulo
        self.anio_edicion = anio_edicion
        self.precio = precio
        self.autor = autor

    @staticmethod
    def json(id, titulo, anio_edicion, precio, autor=None):
        return {'id': id, 'titulo': titulo, 'anio_edicion': anio_edicion, 'precio': precio}
