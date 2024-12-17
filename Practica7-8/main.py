# main.py

from biblioteca import Libro, Revista
from Utils import validar_entero_positivo, validar_cadena_no_vacia, guardar_publicaciones, cargar_publicaciones
from excepciones import ErrorArchivo

publicaciones = []

def menu():
    print("1. Añadir publicaciones (libros o revistas).")
    print("2. Mostrar publicaciones disponibles.")
    print("3. Guardar publicaciones en un fichero.")
    print("4. Cargar publicaciones desde un fichero.")
    print("5. Salir.")

def anadir_publicacion():
    tipo = input("¿Desea añadir un libro o una revista? (libro/revista): ").strip().lower()
    try:
        titulo = validar_cadena_no_vacia(input("Título: "))
        autor = validar_cadena_no_vacia(input("Autor: "))
        anio = validar_entero_positivo(input("Año: "))
        
        if tipo == "libro":
            genero = validar_cadena_no_vacia(input("Género: "))
            publicaciones.append(Libro(titulo, autor, anio, genero))
        elif tipo == "revista":
            num_edicion = validar_entero_positivo(input("Número de Edición: "))
            publicaciones.append(Revista(titulo, autor, anio, num_edicion))
        else:
            print("Tipo de publicación no válido.")
    except ValueError as e:
        print(f"Error: {e}")

def mostrar_publicaciones():
    if not publicaciones:
        print("No hay publicaciones disponibles.")
    else:
        for pub in publicaciones:
            print(pub.Descripcion())

def guardar_en_fichero():
    fichero = input("Nombre del fichero: ").strip()
    try:
        guardar_publicaciones(fichero, publicaciones)
        print("Publicaciones guardadas correctamente.")
    except ErrorArchivo as e:
        print(f"Error: {e}")

def cargar_desde_fichero():
    fichero = input("Nombre del fichero: ").strip()
    try:
        global publicaciones
        publicaciones = cargar_publicaciones(fichero)
        print("Publicaciones cargadas correctamente.")
    except ErrorArchivo as e:
        print(f"Error: {e}")

def main():
    while True:
        menu()
        opcion = input("Seleccione una opción: ").strip()
        if opcion == "1":
            anadir_publicacion()
        elif opcion == "2":
            mostrar_publicaciones()
        elif opcion == "3":
            guardar_en_fichero()
        elif opcion == "4":
            cargar_desde_fichero()
        elif opcion == "5":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()