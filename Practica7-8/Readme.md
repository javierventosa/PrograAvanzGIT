PREGUNTA 1: ¿Cuál es la diferencia entre atributos privados y protegidos en una clase?
-Atributos privados (__atributo) son estrictamente internos a la clase y no deben ser accedidos ni modificados desde fuera de ella, ni siquiera por subclases. Se usan para proteger datos críticos.
Atributos protegidos (_atributo) son más flexibles, ya que pueden ser accedidos y modificados por subclases, aunque por convención no deberían ser manipulados directamente desde fuera de la clase.
PREGUNTA 2: ¿Cómo se maneja la persistencia de datos en Python utilizando ficheros?
-La persistencia de datos en Python utilizando ficheros implica guardar información en archivos para que pueda ser reutilizada en futuras ejecuciones del programa.
PREGUNTA 3: ¿Qué son las excepciones personalizadas y por qué son útiles en la programación?
-Las excepciones personalizadas son clases definidas por el programador que extienden la funcionalidad de las excepciones predefinidas en un lenguaje de programación. En Python, se crean derivando una clase de base de excepciones, como Exception.
Permiten modelar errores específicos de tu aplicación, en lugar de depender únicamente de las excepciones genéricas que ofrece el lenguaje.
PREGUNTA 4:¿Cómo se define y utiliza un constructor en una clase en Python?
-Un constructor en Python es un método especial que se utiliza para inicializar los atributos de una clase cuando se crea una instancia de esta. En Python, el constructor es el método llamado __init__.
PREGUNTA 5: ¿Qué es JSON y cómo se utiliza para la persistencia de datos en esta práctica?
JSON (JavaScript Object Notation) es un formato de texto ligero utilizado para estructurar y almacenar datos de forma legible tanto para humanos como para máquinas. Es ampliamente utilizado en aplicaciones para intercambiar datos entre sistemas, como APIs, y también para la persistencia de datos.
JSON representa los datos como pares clave-valor anidados en estructuras como objetos y arrays, similares a diccionarios y listas en Python.
PREGUNTA 6: ¿Qué es la polimorfismo en la programación orientada a objetos y cómo se puede aplicar en Python?
-El polimorfismo es un principio fundamental de la programación orientada a objetos (POO) que permite que una misma interfaz o método sea utilizado por diferentes tipos de objetos. En otras palabras, es la capacidad de un objeto para comportarse de diferentes maneras dependiendo de su tipo.
El término proviene del griego y significa "muchas formas". Esto permite escribir código más genérico, reutilizable y flexible.
PREGUNTA 7: ¿Qué es la serialización de objetos y cómo se utiliza en Python?
-La serialización es el proceso de convertir un objeto en memoria (como una lista, diccionario, o instancia de clase) en un formato que puede almacenarse o transmitirse y luego ser reconstruido (deserializado) en otro entorno o tiempo. Este formato puede ser texto (por ejemplo, JSON o XML) o binario (por ejemplo, con pickle en Python).
