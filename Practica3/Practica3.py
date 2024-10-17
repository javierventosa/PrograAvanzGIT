from time_management import Time

def main():
    time_obj = Time()
    while True:
        print("\nMenú:")
        print("1. Introducir una nueva hora")
        print("2. Visualizar hora")
        print("3. Crear una hora a partir de una cadena (formato HH:MM:SS FORMAT)")
        print("4. Terminar")
        choice = input("Elige una opción (1-4): ")

        if choice == '1':
            try:
                nHoras = int(input("Introduce las horas: "))
                nMinutos = int(input("Introduce los minutos: "))
                nSegundos = int(input("Introduce los segundos: "))
                pszFormato = input("Introduce el formato (AM, PM, 24 HOURS): ").upper()
                if time_obj.set_time(nHoras, nMinutos, nSegundos, pszFormato):
                    print("Hora establecida correctamente.")
                else:
                    print("Hora no válida.")
            except ValueError:
                print("Entrada no válida. Por favor, introduce números enteros para horas, minutos y segundos.")
        elif choice == '2':
            print(f"La hora actual es:", {time_obj.get_time()})
        elif choice == '3':
            time_string = input("Introduce la hora en formato HH:MM:SS FORMAT: ")
            new_time_obj = Time.from_string(time_string)
            if new_time_obj:
                time_obj = new_time_obj
                print("Hora creada correctamente a partir de la cadena:")
            else:
                print("No se pudo crear la hora a partir de la cadena proporcionada.")
        elif choice == '4':
            print("Terminando el programa.")
            break
        else:
            print("Opción no válida. Por favor elige una opción del 1 al 4.")

if __name__ == "__main__":
    main()