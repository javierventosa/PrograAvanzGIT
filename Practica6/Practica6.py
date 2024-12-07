from datetime import time

class Ficha:
    def __init__(self, nombre="", edad=0, nacio=time(0, 0, 0)):
        self._nombre = nombre
        self._edad = edad
        self._nacio = nacio

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, value):
        self._nombre = value

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, value):
        self._edad = value

    @property
    def nacio(self):
        return self._nacio

    @nacio.setter
    def nacio(self, value):
        self._nacio = value

    def Visualizar(self):
        print(f"Nombre: {self._nombre}, Edad: {self._edad}, Nació: {self._nacio}")

class Empleado(Ficha):
    def __init__(self, nombre="", edad=0, nacio=time(0, 0, 0), categoria="", antiguedad=0):
        super().__init__(nombre, edad, nacio)
        self._categoria = categoria
        self._antiguedad = antiguedad

    @property
    def categoria(self):
        return self._categoria

    @categoria.setter
    def categoria(self, value):
        self._categoria = value

    @property
    def antiguedad(self):
        return self._antiguedad

    @antiguedad.setter
    def antiguedad(self, value):
        self._antiguedad = value

    def Visualizar(self):
        super().Visualizar()
        print(f"Categoría: {self._categoria}, Antigüedad: {self._antiguedad} años")

class Cliente(Ficha):
    def __init__(self, nombre="", edad=0, nacio=time(0, 0, 0), dni=""):
        super().__init__(nombre, edad, nacio)
        self._dni = dni

    @property
    def dni(self):
        return self._dni

    @dni.setter
    def dni(self, value):
        self._dni = value

    def Visualizar(self):
        super().Visualizar()
        print(f"DNI: {self._dni}")

    def __eq__(self, other):
        if isinstance(other, Cliente):
            return self.nombre == other.nombre and self.edad == other.edad
        return False

class RegistroDiario:
    def __init__(self):
        self._personas = []

    def agregar_persona(self, persona):
        if isinstance(persona, (Empleado, Cliente)):
            self._personas.append(persona)
        else:
            raise ValueError("Solo se pueden agregar objetos de tipo Empleado o Cliente")

    def visualizar_registro(self):
        for persona in self._personas:
            persona.Visualizar()

    def visualizar_empleados(self):
        for persona in self._personas:
            if isinstance(persona, Empleado):
                persona.Visualizar()

    def es_empleado(self, persona):
        return isinstance(persona, Empleado)

    def __getitem__(self, index):
        return self._personas[index]

    def __add__(self, other):
        if isinstance(other, RegistroDiario):
            nuevo_registro = RegistroDiario()
            nuevo_registro._personas = self._personas + other._personas
            return nuevo_registro
        else:
            raise ValueError("Solo se pueden combinar objetos de tipo RegistroDiario")