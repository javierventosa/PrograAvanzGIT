from typing import List
import uuid

def leer_int(prompt: str) -> int:
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Error: Debe ingresar un número entero.")

def leer_float(prompt: str) -> float:
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Error: Debe ingresar un número decimal.")

def crear_menu(options: List[str]) -> int:
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    return leer_int("Seleccione una opción: ")

def generar_id_unico() -> str:
    return str(uuid.uuid4())[:8]
