import numpy as np

class CMatFloat:
    """
    Clase que representa una matriz dinámica 1D/2D.
    Atributos:
    _Matriz # Almacena la matriz (utilice numpy)
    _m_nFilas # Almacena el número de filas de la matriz
    _m_nColumnas # Almacena el número de columnas de la matriz
    """
    def __init__(self):
        """
        Método para inicializar el atributo matriz con None
        y los atributos filas y columnas a 0.
        """
        self.matriz = None
        self.nFilas = 0
        self.nColumnas = 0

    def CrearMatriz2D(self, nFilas, nColumnas):
        """
        Método para crear una matriz bidimensional de ceros.
        Asigna valores de filas y columnas según parámetros.
        """
        self.nFilas = nFilas
        self.nColumnas = nColumnas
        self.matriz = np.zeros((self.nFilas, self.nColumnas))

    def CrearMatriz1D(self, nElementos):
        """
        Método para crear una matriz unidimensional de ceros.
        Usa CrearMatriz2D para asignar 1 fila y n columnas.
        """
        self.CrearMatriz2D(1, nElementos)

    def Introducir(self):
        """
        Método para introducir los elementos de la matriz.
        Los elementos de la matriz son de tipo decimal.
        """
        for i in range(self.nFilas):
            for j in range(self.nColumnas):
                self.matriz[i][j] = leer_float(f"Introduce el elemento [{i}, {j}]: ")

    def Mostrar(self):
        """
        Método para mostrar los elementos de la matriz.
        """
        if self.matriz is not None:
            print(self.matriz)
        else:
            print("La matriz no está creada.")

    def Existe(self):
        """
        Método que verifica si matriz está creada y no está vacía.
        Retorna True si existe, de lo contrario retorna False.
        """
        return self.matriz is not None and self.matriz.size > 0

    def SumarMatrices(self, otra_matriz):
        """
        Método que suma la matriz actual con otra matriz.
        Parámetros:
        otra_matriz: objeto de CMatFloat con la matriz a sumar.
        Retorna:
        numpy.ndarray: La matriz resultante de la suma.
        """
        if self.nFilas != otra_matriz.nFilas or self.nColumnas != otra_matriz.nColumnas:
            raise ValueError("Las dimensiones de las matrices no coinciden")
        return self.matriz + otra_matriz.matriz

    def RestarMatrices(self, otra_matriz):
        """
        Método que resta la matriz actual con otra matriz.
        Parámetros:
        otra_matriz: objeto de CMatFloat con la matriz a restar.
        Retorna:
        numpy.ndarray: La matriz resultante de la resta.
        """
        if self.nFilas != otra_matriz.nFilas or self.nColumnas != otra_matriz.nColumnas:
            raise ValueError("Las dimensiones de las matrices no coinciden")
        return self.matriz - otra_matriz.matriz

def leer_int(mensaje="Introduce un número entero: "):
    """
    Función auxiliar que lee un número entero del teclado.
    Si se introduce un valor no válido, se solicita de nuevo.
    Parámetros:
    mensaje (str): El mensaje que se muestra al usuario
    solicitando la entrada.
    Retorna:
    int: El valor entero introducido por el usuario.
    """
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Entrada no válida. Por favor, introduce un número entero.")

def leer_float(mensaje="Introduce un número decimal: "):
    """
    Función auxiliar que solicita al usuario un número decimal.
    Si se introduce un valor no válido, se solicita de nuevo.
    Parámetros:
    mensaje (str): El mensaje que se muestra al usuario
    solicitando la entrada.
    Retorna:
    float: El valor decimal introducido por el usuario.
    """
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Entrada no válida. Por favor, introduce un número decimal.")

def crear_menu(opciones_menu):
    """
    Función que muestra un menú de opciones y solicita al usuario
    que seleccione una opción válida.
    Parámetros:
    opciones_menu (list): lista de opciones a mostrar en el menú.
    Retorna:
    int: El número de opción seleccionado por el usuario.
    """
    while True:
        print("\nMenú de opciones:")
        for i, opcion in enumerate(opciones_menu, 1):
            print(f"{i}. {opcion}")
        try:
            opcion_seleccionada = int(input("Selecciona una opción: "))
            if 1 <= opcion_seleccionada <= len(opciones_menu):
                return opcion_seleccionada
            else:
                print("Opción no válida. Por favor, selecciona una opción del menú.")
        except ValueError:
            print("Entrada no válida. Por favor, introduce un número entero.")

def menu_principal():
    matriz = CMatFloat()
    while True:
        opciones = [
            "Construir matriz 1D",
            "Construir matriz 2D",
            "Introducir matriz",
            "Mostrar matriz",
            "Operaciones con matrices",
            "Terminar"
        ]
        opcion = crear_menu(opciones)

        if opcion == 1:
            nElementos = leer_int("Introduce el número de elementos: ")
            matriz.CrearMatriz1D(nElementos)
        elif opcion == 2:
            nFilas = leer_int("Introduce el número de filas: ")
            nColumnas = leer_int("Introduce el número de columnas: ")
            matriz.CrearMatriz2D(nFilas, nColumnas)
        elif opcion == 3:
            matriz.Introducir()
        elif opcion == 4:
            matriz.Mostrar()
        elif opcion == 5:
            menu_operaciones(matriz)
        elif opcion == 6:
            print("Terminando el programa.")
            break

def menu_operaciones(matriz):
    while True:
        opciones = [
            "Sumar matrices",
            "Restar matrices",
            "Volver al menú principal"
        ]
        opcion = crear_menu(opciones)

        if opcion == 1:
            otra_matriz = CMatFloat()
            nFilas = leer_int("Introduce el número de filas de la segunda matriz: ")
            nColumnas = leer_int("Introduce el número de columnas de la segunda matriz: ")
            otra_matriz.CrearMatriz2D(nFilas, nColumnas)
            otra_matriz.Introducir()
            resultado = matriz.SumarMatrices(otra_matriz)
            print("Resultado de la suma de matrices:")
            print(resultado)
        elif opcion == 2:
            otra_matriz = CMatFloat()
            nFilas = leer_int("Introduce el número de filas de la segunda matriz: ")
            nColumnas = leer_int("Introduce el número de columnas de la segunda matriz: ")
            otra_matriz.CrearMatriz2D(nFilas, nColumnas)
            otra_matriz.Introducir()
            resultado = matriz.RestarMatrices(otra_matriz)
            print("Resultado de la resta de matrices:")
            print(resultado)
        elif opcion == 3:
            break

if __name__ == "__main__":
    menu_principal()