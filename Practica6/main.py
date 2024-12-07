from datetime import time
from Practica6 import Empleado, Cliente, RegistroDiario
import Utils

def main():
    registro = RegistroDiario()
    otro_registro = RegistroDiario()

    while True:
        Utils.mostrar_menu()
        opcion = Utils.leer_opcion()

        if opcion == 1:
            try:
                nombre = Utils.leer_cadena("Nombre del empleado: ")
                edad = int(input("Edad del empleado: "))
                nacio = time.fromisoformat(input("Hora de nacimiento (HH:MM:SS): "))
                categoria = Utils.leer_cadena("Categoría del empleado: ")
                antiguedad = int(input("Antigüedad del empleado: "))
                empleado = Empleado(nombre, edad, nacio, categoria, antiguedad)
                registro.agregar_persona(empleado)
                print("Empleado agregado correctamente.")
            except Exception as e:
                print(f"Error al agregar empleado: {e}")

        elif opcion == 2:
            try:
                nombre = Utils.leer_cadena("Nombre del cliente: ")
                edad = int(input("Edad del cliente: "))
                nacio = time.fromisoformat(input("Hora de nacimiento (HH:MM:SS): "))
                dni = Utils.leer_cadena("DNI del cliente: ")
                cliente = Cliente(nombre, edad, nacio, dni)
                registro.agregar_persona(cliente)
                print("Cliente agregado correctamente.")
            except Exception as e:
                print(f"Error al agregar cliente: {e}")

        elif opcion == 3:
            nombre = Utils.leer_cadena("Nombre de la persona: ")
            edad = int(input("Edad de la persona: "))
            for persona in registro._personas:
                if persona.nombre == nombre and persona.edad == edad:
                    persona.Visualizar()
                    if isinstance(persona, Empleado):
                        print("Tipo: Empleado")
                    else:
                        print("Tipo: Cliente")
                    break
            else:
                print("Persona no encontrada.")

        elif opcion == 4:
            registro.visualizar_registro()

        elif opcion == 5:
            registro.visualizar_empleados()

        elif opcion == 6:
            indice = int(input("Índice de la persona: "))
            if 0 <= indice < len(registro._personas):
                registro[indice].Visualizar()
            else:
                print("Índice fuera de los límites del registro.")

        elif opcion == 7:
            # Aquí se puede agregar personas a otro_registro para la combinación
            registro_combinado = registro + otro_registro
            registro_combinado.visualizar_registro()

        elif opcion == 8:
            break

        else:
            print("Opción no válida. Inténtelo de nuevo.")

if __name__ == "__main__":
    main()