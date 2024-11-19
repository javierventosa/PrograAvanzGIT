def operation_logger(func):
    def wrapper(*args, **kwargs): # Se utiliza *args para recibir múltiples argumentos
        operation_name = func.__name__ # Se obtiene el nombre de la función
        result = func(*args, **kwargs) #Se ejecuta la función con los argumentos recibidos
        print(f"Operation: {operation_name}, Inputs: {args}, Result: {result}") # Se imprime el nombre de la operación, los argumentos y el resultado
        return result # Se retorna el resultado de la operación
    return wrapper

add = lambda *args: sum(args) # Se utiliza sum para sumar los argumentos recibidos
subtract = lambda a, b: a - b # Se realiza la resta de los argumentos recibidos
multiply = lambda *args: eval('*'.join(map(str, args))) # Se realiza la multiplicación de los argumentos recibidos
divide = lambda a, b: a / b if b != 0 else 'Error: Division by zero' # Se realiza la división de los argumentos recibidos, si el segundo argumento es 0 se retorna un mensaje de error

@operation_logger
def math_operation(operation, *args): # Se recibe la operación funciones lambda y los argumentos
    try:
        return operation(*args) # Se ejecuta la operación con los argumentos recibidos
    except ZeroDivisionError: # Se maneja el error de división por 0
        return 'Error: Division by zero'

# Pruebas
print(math_operation(add, 5, 3))
print(math_operation(subtract, 10, 4))
print(math_operation(multiply, 2, 6))
print(math_operation(divide, 15, 3))
print(math_operation(divide, 10, 0))  # Debe manejar la división por 0
print(math_operation(add, 1, 2, 3, 4, 5))  # Debe manejar múltiples argumentos