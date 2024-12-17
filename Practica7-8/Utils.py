# utils.py

import json
from excepciones import ErrorArchivo
from biblioteca import Libro, Revista

def validar_entero_positivo(valor):
    try:
        entero = int(valor)
        if entero <= 0:
            raise ValueError("El valor debe ser un entero positivo.")
        return entero
    except ValueError as e:
        raise ValueError(f"Error de validación: {e}")

def validar_cadena_no_vacia(valor):
    if not valor.strip():
        raise ValueError("El valor no puede estar vacío.")
    return valor

def guardar_publicaciones(fichero, publicaciones):
    try:
        with open(fichero, 'w') as f:
            json.dump([pub.__dict__ for pub in publicaciones], f)
    except Exception as e:
        raise ErrorArchivo(f"Error al guardar el fichero: {e}")

def cargar_publicaciones(fichero):
    try:
        with open(fichero, 'r') as f:
            datos = json.load(f)
            publicaciones = []
            for dato in datos:
                if '_genero' in dato:
                    publicaciones.append(Libro(**dato))
                elif '_num_edicion' in dato:
                    publicaciones.append(Revista(**dato))
            return publicaciones
    except Exception as e:
        raise ErrorArchivo(f"Error al cargar el fichero: {e}")
