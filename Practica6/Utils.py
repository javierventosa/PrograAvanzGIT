from typing import List
import uuid

def leer_int(mensaje: str) -> int:
    while True:
        try:
            value = int(input(mensaje))
            return value
        except ValueError:
            print("Error: Debe ingresar un número entero.")

def leer_float(mensaje: str) -> float:
    while True:
        try:
            value = float(input(mensaje))
            return value
        except ValueError:
            print("Error: Debe ingresar un número decimal.")

def crear_menu(options: List[str]) -> int:
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")

def generar_id_unico() -> str:
    return str(uuid.uuid4())[:8]

def leer_cadena(mensaje):
    while True:
        cadena = input(mensaje)
        if cadena:
            return cadena
        else:
            print("La cadena no puede estar vacía. Inténtelo de nuevo.")

def mostrar_menu():
    opciones = [
        "Introducir empleado",
        "Introducir cliente",
        "Buscar por nombre (y edad)",
        "Mostrar registro diario",
        "Mostrar empleados",
        "Visualizar persona por índice",
        "Combinar registros diarios",
        "Salir"
    ]
    crear_menu(opciones)

def leer_opcion():
    while True:
        try:
            opcion = int(input("Seleccione una opción: "))
            if 1 <= opcion <= 8:
                return opcion
            else:
                print("Opción no válida. Inténtelo de nuevo.")
        except ValueError:
            print("Entrada no válida. Por favor, introduzca un número.")
