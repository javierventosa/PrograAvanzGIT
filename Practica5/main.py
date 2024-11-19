from book import Book
from library import Library
from user import User
from utils import crear_menu, leer_int, generar_id_unico

def main():
    biblioteca = Library()
    usuarios = []

    while True:
        opcion = crear_menu([
            "Añadir libro",
            "Eliminar libro",
            "Registrar usuario",
            "Realizar préstamo",
            "Realizar devolución",
            "Mostrar todos los libros",
            "Salir"
        ])

        if opcion == 1:
            titulo = input("Ingrese el título del libro: ")
            autor = input("Ingrese el autor del libro: ")
            isbn = input("Ingrese el ISBN del libro: ")
            libro = Book(titulo, autor, isbn)
            biblioteca.add_book(libro)
            print("Libro añadido con éxito.")

        elif opcion == 2:
            isbn = input("Ingrese el ISBN del libro a eliminar: ")
            biblioteca.remove_book(isbn)
            print("Libro eliminado.")

        elif opcion == 3:
            nombre = input("Ingrese el nombre del usuario: ")
            user_id = generar_id_unico()
            usuario = User(nombre, user_id)
            usuarios.append(usuario)
            print(f"Usuario registrado con ID: {user_id}")

        elif opcion == 4:
            isbn = input("Ingrese el ISBN del libro a prestar: ")
            if biblioteca.borrow_book(isbn):
                print("Préstamo realizado.")
            else:
                print("No se pudo realizar el préstamo. Verifique el ISBN o la disponibilidad.")

        elif opcion == 5:
            isbn = input("Ingrese el ISBN del libro a devolver: ")
            if biblioteca.return_book(isbn):
                print("Devolución realizada.")
            else:
                print("No se pudo realizar la devolución. Verifique el ISBN.")

        elif opcion == 6:
            print(biblioteca.show_books())

        elif opcion == 7:
            print("Saliendo del sistema de gestión de bibliotecas.")
            break

if __name__ == "__main__":
    main()
