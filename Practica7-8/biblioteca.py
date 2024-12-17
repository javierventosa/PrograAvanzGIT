# biblioteca.py

class Publicacion:
    def __init__(self, titulo, autor, anio):
        self._titulo = titulo
        self._autor = autor
        self._anio = anio

    @property
    def titulo(self):
        return self._titulo

    @titulo.setter
    def titulo(self, value):
        self._titulo = value

    @property
    def autor(self):
        return self._autor

    @autor.setter
    def autor(self, value):
        self._autor = value

    @property
    def anio(self):
        return self._anio

    @anio.setter
    def anio(self, value):
        self._anio = value

    def Descripcion(self):
        return f"Título: {self.titulo}, Autor: {self.autor}, Año: {self.anio}"

class Libro(Publicacion):
    def __init__(self, titulo, autor, anio, genero):
        super().__init__(titulo, autor, anio)
        self._genero = genero

    @property
    def genero(self):
        return self._genero

    @genero.setter
    def genero(self, value):
        self._genero = value

    def Descripcion(self):
        return f"{super().Descripcion()}, Género: {self.genero}"

class Revista(Publicacion):
    def __init__(self, titulo, autor, anio, num_edicion):
        super().__init__(titulo, autor, anio)
        self._num_edicion = num_edicion

    @property
    def num_edicion(self):
        return self._num_edicion

    @num_edicion.setter
    def num_edicion(self, value):
        self._num_edicion = value

    def Descripcion(self):
        return f"{super().Descripcion()}, Número de Edición: {self.num_edicion}"