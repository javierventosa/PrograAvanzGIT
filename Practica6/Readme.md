PREGUNTA 1: ¿Por qué es útil utilizar métodos @property y @setter en una clase en Python?
-Los métodos @property y @setter son útiles en Python porque permiten una forma limpia y controlada de gestionar el acceso y la modificación de los atributos de una clase.
PREGUNTA 2: ¿Por qué es importante el encapsulamiento en la programación orientada a objetos?
-Por la protección de datos, abstracción y simplicidad, facilita el mantenimiento y la evolución del código, reutilización y modularidad y mejora la seguridad del sistema.
PREGUNTA 3: ¿Cómo se puede extender la funcionalidad de una clase en Python mediante la herencia?
-La herencia en Python permite que una clase (llamada subclase o clase hija) extienda la funcionalidad de otra clase (llamada superclase o clase padre). Esto se logra reutilizando atributos y métodos de la superclase, y agregando o sobrescribiendo características según sea necesario.
PREGUNTA 4: ¿Qué es la sobrecarga de métodos y cómo se puede implementar en Python?
-La sobrecarga de métodos ocurre cuando se definen múltiples métodos con el mismo nombre pero diferentes parámetros en una clase.  Sin embargo, Python no soporta sobrecarga de métodos de manera directa, porque no permite múltiples definiciones del mismo método en una clase. Si intentas definir un método con el mismo nombre más de una vez, la definición más reciente sobrescribe las anteriores.
A pesar de esta limitación, Python permite simular la sobrecarga de métodos utilizando: argumentos por defecto, uso de *args y **kwargs, sobrecarga manual mediante lógica condicional
PREGUNTA 5: ¿Cuál es la diferencia entre un método de clase y un método de instancia en Python?
-Un método de instancia está diseñado para operar sobre instancias específicas de la clase, utilizando el objeto como contexto (a través de self). Un método de clase está diseñado para operar a nivel de la clase misma, utilizando la clase como contexto (a través de cls).
PREGUNTA 6: ¿Cómo se podría implementar un método __str__ en la clase Ficha para proporcionar una representación en cadena de una instancia?
-Para implementar un método __str__ en la clase Ficha que proporcione una representación en cadena de una instancia, puedes definir el método __str__ dentro de la clase. Este método debe devolver una cadena que describa la instancia de manera legible.
PREGUNTA 7: ¿Cómo se puede implementar un método en la clase Ficha para calcular la edad de una persona basada en su fecha de nacimiento?
-Para implementar un método en la clase Ficha que calcule la edad de una persona basada en su fecha de nacimiento, primero necesitas cambiar el tipo del atributo 'nacio' de time a date para que incluya la información de la fecha completa (año, mes y día). Luego, puedes usar la biblioteca datetime para calcular la diferencia entre la fecha actual y la fecha de nacimiento
