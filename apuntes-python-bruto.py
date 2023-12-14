##########################
# Seccion 2: Tipos básicos
##########################

# Strings

from pprint import pprint
nombre_curso = "Ultimate Python"
descripcion_curso = """
Ultimate Python,
este curso contempla todos los conocimientos
que necesitas aprender para 
un trabajo como programador.
"""
print(nombre_curso, descripcion_curso)

len(nombre_curso)   # => 15 Número de caracteres
nombre_curso[0]     # => 'U'
nombre_curso[0:8]   # => 'Ultimate' Susbtring pos 0 hasta pos 7
nombre_curso[9:]    # => 'Python' Substring desde 9 hasta el final
nombre_curso[:8]    # => 'Ultimate' Substring desde al principio hasta pos 7
nombre_curso[:]     # => 'Ultimate Python

# Formato de string
nombre = "Michael"
apellido = "Singer"
# Entre llaves puedo usar cualquier expresión
nombre_completo = f"{nombre} {apellido[0]}"

# Métodos de string
animal = "orniTORRinco sibeRIANO"
animal.upper()        # => 'ORNITORRINCO SIBERIANO'
animal.lower()        # => 'ornitorrinco suberiano'
animal.capitalize()   # => 'Ornitorrinco siberiano'
animal.title()        # => 'Ornitorrinco Siberiano'

animal.strip()        # Quita espacios a izq y dcha
animal.lstrip()       # Quita espacios a izq
animal.rstrip()       # Quita espacios a dcha

animal.find("TORR")   # => 4 Busca índice en string. Si no encuentra: -1

animal.replace("TORR", "J")  # => 'orniJinco sibeRIANO"

"TORR" in animal      # => True
"TORR" not in animal  # => False

# Secuencias de escape
curso = "Ultimate \"Python\""  # => Ultimate "Python"
curso = "Ultimate \'Python\'"  # => Ultimate 'Python'
curso = "Ultimate \\Python\\"  # => Ultimate \Python\
curso = "Ultimate \nPython"    # => Salto de línea

# Números
numero = 2
decimal = 1.2
imaginario = 2 + 2j

1 + 3   # Suma
1 - 3   # Resta
1 * 3   # Multiplicación
1 / 3   # División
1 // 3  # Cociente
1 % 3   # Resto
2 ** 3  # Potencia

numero += 2  # Forma corta
numero -= 2
numero *= 2
numero /= 2

# Módulo Math
round(1.3)  # => '1' Redonndeo
round(1.7)  # => '2' Redonndeo
round(1.5)  # => '2' Redonndeo

abs(-34)  # => '34' Valor absoluto

# import math
# docs.python.org/library/math
math.ceil(1.1)  # => '2' Entero superior
math.floor(1.999)  # => '1' Entero inferior
math.isnan(23)  # => False. Comprueba que no es un número
math.pow(10, 3)  # => '1000' 10 elevado a 3
math.sqrt(9)    # => 3 Raíz cuadrada

# Conversión de tipos
int()
str()
float()
bool("")  # => False
bool("0")  # => True
bool(None)  # => False
bool(" ")  # => True
bool(0)  # => False

#############################
# Seccion 3: Control de flujo
#############################

# Comparadores lógicos
1 > 2
1 < 2
1 <= 2
1 >= 2
2 == 2
2 == "2"
2 != "2"
2 != 2  # => False

# if, else, elif
edad = 15
if edad > 54:
    print("Puede ver la película con descuento")
elif edad > 17:
    print("Puede ver la película")
else:
    print("No puedes entrar")

# Operador ternario
mensaje = "Es mayor" if edad > 17 else "Es menor"

# Operadores lógicos: son operaciones de cortocircuito
# Si de izquierda a deracha, algún valor determina la expresión
# no se siguen evaluando el resto de condiciones hacia la derecha

gas = True
encendido = True
edad = 18

if not gas and (encendido or edad > 17):
    print("Puedes avanzar")

# Cadena de comparadores
if 15 <= edad <= 65:
    print("Puedo continuar")

# For
for numero in range(5):
    print(numero)

# For else
buscar = 10

for numero in range(5):
    print(numero)
    if numero == buscar:
        print("Numero encontrado")
        break
else:
    print("No encontré el número")

# Iterables
# Listas, tuplas y strings, son iterables, es decir, se pueden recorrer con un for
for char in "Ultimate Python":
    print(char)

# While
comando = ""

while comando.lower() != "salir":
    comando = input("$ ")  # Solicita texto en consola
    print(comando)

# Loop infinito
while True:
    comando = input("$ ")
    print(comando)
    if comando.lower() == "salir":
        break  # Agregar condición de salida para poder romper el loop infinito

# Loop anidado: Tratar de evitarlos salvo que no quede más remedio.
# Con listas muy grandes consumen muchos recursos.
for j in range(3):
    for k in range(2):
        print(f"{j} {k}")


# Ejercicio: Calculadora
print("Bienvenidos a la calculadora")
print("Para salir escribe Salir")
print("Las operaciones son suma, multi, div y resta")

comenzar = True
acumulador = input("Ingresa número: ")

if acumulador == "Salir":
    comenzar = False
else:
    acumulador = int(acumulador)


while comenzar:
    operacion = input("Ingresa operación: ")
    if operacion == "Salir":
        break

    numero = input("Ingresa siguiente número: ")
    if numero == "Salir":
        break

    numero = int(numero)

    if operacion == "suma":
        acumulador += numero

    elif operacion == "multi":
        acumulador *= numero
    elif operacion == "div":
        acumulador /= numero
    elif operacion == "resta":
        acumulador -= numero
    else:
        print("Operación no conocida")
        break

    print(f"El resultado es {acumulador}")


#############################
# Seccion 4: Funciones
#############################

# Introducción
def hola():
    print("Hola Mundo!")


hola()

# Parámetros y argumentos


def hola(nombre, apellido):  # Parámetros
    print(f"Hola {nombre} {apellido}")


hola("Marcus", "Sheiner")  # Argumentos

# Argumentos opcionales


def hola(nombre, apellido="Strauss"):  # Parámetros
    print(f"Hola {nombre} {apellido}")


hola("Marcus")  # => "Hola Marcus Strauss"
hola("Marcus", "Tobías")  # => "Hola Marcus Tobías"

# Argumenos nombrados
# => Tengo que nombrar todos necesariamente
hola(apellido="Tobías", nombre="David")

# Xarg: Un iterable como argumento


def sum(*numeros):  # El * indica que 'números' es un iterable
    resultado = 0
    for numero in numeros:
        resultado += numero
    print(resultado)


suma(2, 4, 55, 67, 7)

# Kwargs: Argumentos clave-valor (key-word args)


def get_product(**datos):  # El ** indica que es un diccionario clave-valor
    print(datos)
    print(datos["id"], datos["name"], datos["desc"])


get_product(id="23",
            name="iPhone",
            desc="Esto es un iPhone")

# Return


def suma(a, b):
    resultado = a + b
    return resultado


suma(1, 3)

# Alcance:

saludo = "Hola global"


def saludar_local():
    saludo = "Hola mundo"


def saludar_global():
    global saludo  # Solo usarlo de manera excepcional. Mala pŕactica
    saludo = "Hola mundo"


saludar_local()
print(saludo)
saludar_global()  # Cambia la variable global
print(saludo)

# Depurando funciones
# Must!

# Ejercicio: Palíndromo


def es_palindromo(texto):
    texto = texto.lower()           # Convierto a minúsculas
    texto = texto.replace(" ", "")  # Quito espacios en blanco
    return texto[::-1] == texto     # Invierto el texto


texto = "Amo la paloma"
print(texto, es_palindromo(texto))


#############################
# Seccion 5: Tipos avanzados
#############################

# Listas
numeros = [1, 2, 3]
letras = ["a", "b", "c"]
booleans = [True, False, True, True]
matriz = [[0, 1], [0, 1]]
ceros = [0] * 10
alfanumerico = numeros + letras
# A list le tenemos que pasar un Iterable
rango = list(range(10))  # => 0 a 9
rango = list(range(1, 11))  # => 1 a 10
chars = list("hola mundo")  # => ['h', 'o', 'l', ....]

# Manipulando listas
mascotas = ["Tobi", "Dogy", "Sazam", "Copito"]
mascotas[0] 			# Recoge el primer elemento
mascotas[0] = "Dave" 	# Reasigna
mascotas[2:]			# Recoge desde la posición 2 al final
mascotas[-1]			# Último
mascotas[::2]			# Tomta de dos en dos
mascotas[1::2]			# Comienza desde posición 1 y de dos en dos hasta el final
mascotas[1:2:2]			# Comienza desde posición 1 y de dos en dos hasta el 2

numeros = list(range(21))
numeros[::2]			# Números pares
numeros[1::2]			# Números impares

# Desempaquetar listas
numeros = [1, 2, 3, 4, 5]
primero, *otros = numeros  # primero => 1, otros => [2, 3, 4, 5]
primero, segundo, *otros, penu, ultimo = numeros  # "otros" será Iterable

# Iterar listas
mascotas = ["Pelusa", "Pulga", "Tobi", "Rocky"]
for mascota in enumerate(mascotas):
    print(mascota)  # => Devuelve tuplas (0, 'Pelusa), (1, 'Pulga') ...
    print(mascota[0])  # => 0 1 ...
    print(mascota[1])  # => Pelusa Pulga ...

# Con índice
for indice, mascota in enumerate(mascotas):
    print(indice, mascota)  # => Devuelve 0 'Pelusa' ...

# Buscando elementos
mascotas = ["Pelusa", "Pulga", "Tobi", "Rocky", "Pulga"]

mascotas.index("Pulga")  # => 1
mascotas.index("Noexiste")  # => Error
if "Noexiste" in mascotas:
    mascotas.index("Noexiste")

mascotas.count("Pulga")  # => 2

# Agregando y eliminando elementos a un listado
mascotas = ["Pelusa", "Pulga", "Tobi", "Rocky", "Pulga"]

mascotas.insert(1, "Dave") 	# Ingresamos Dave en la posición 1
mascotas.append("Melvin") 	# Ingresamos Melvin al final
mascotas.remove("Pulga") 	# Elimina la primera ocurrencia
# Si queremos eliminar más de una ocurrencia tendremos que contar con count y ejecutar remove tantas veces
mascotas.pop()				# Elimino el último
mascotas.pop(1)			# Saca el elemento 1
del mascotas[1]				# Otra forma de eliminar el elemento 1
mascotas.clear()			# Vacía la lista

# Ordenando listas
numeros = [3, 55, 334, 4, 6, 76, 45]
numeros.sort()					# Ordena
numeros.sort(reverse=True)		# Orden descendente
sorted(numeros)					# Devuelve una NUEVA lista pero no modifica el original
sorted(numeros, reverse=True)  # Idem en orden descendente

usuarios = [[4, "David"], [1, "María"], [5, "Begoña"], [9, "Eladio"]]
usuarios.sort()		# Ordena según primer argumento

# Cambia la película, ordenamos según el segundo elemento
usuarios = [["David", 4], ["María", 1], ["Begoña", 5], ["Eladio", 9]]


def ordena(elemento):
    return elemento[1]


# No ponemos 'ordena()', solo 'ordena', porque queremos pasar la referencia y no ejecturla
usuarios.sort(key=ordena)
usuarios.sort(key=ordena, reverse=True)

# Buscamos una forma más elegante de pasar un función a sort

# Expresiones lambda (o funciones anónimas)
# usuarios.sort(key=lambda parametros: valorRetorno, reverse=True)
# Estas funciones anónimas son recomendables si las utilizamos solo una vez como en este caso
usuarios.sort(key=lambda el: el[1], reverse=True)

# Compresión de listas
# Sintaxis: nombres = [expresion for item in items]
usuarios = [["David", 4], ["María", 1], ["Begoña", 5], ["Eladio", 9]]

# moficación de lista (MAP)
# => ["David", "María", "Begoña", "Eladio"]
nombres = [usuario[0] for usuario in usuarios]

# filtrar usuarios con id > 2 (FILTER)
nombres = [usuario for usuario in usuarios if usuario[1] > 2]

# modificar + filtrar usuarios con id > 2
nombres = [usuario[0] for usuario in usuarios if usuario[1] > 2]

# Map y filter (alternativa a lo anterior)
# Los programadores que preferien la programación funcional prefieren map o filter
nombres = list(map(lambda usuario: usuario[0], usuarios))  # MAP
menosUsuarios = list(
    filter(lambda usuario: usuario[1] > 2, usuarios))  # FILTER

# Tuplas (paréntesis redondos)
# Una tupla es lo mismo que una lista, con la salvedad de que no se puede modificar
# La usamos cuando no queramos modificar sus elementos
# Las operaciones son las mismas que las de las listas salvo las que modifique la tupla
# Podemos: manipular, desempaquetar e iterar
numeros = (1, 2, 3) + (4, 5, 6)  # => (1, 2, 3, 4, 5, 6)

# Lista a Tupla. Tuple recibe cualquier cosa que sea Iterable
punto = tuple([1, 2])

# Para modificar una tupla, creo primero un lista en base a la tupla
lista_numero = list(numeros)

# Sets (conjuntos o grupos)
# Es una colección de datos que no se puede repetir y que tampoco está ordenada
primer = {1, 1, 2, 2, 3, 4}
# => {1, 2, 3, 4} Python quita los duplicados en el momento de usar el set
print(primer)

primer.add(5)
primer.remove(1)


primer = {1, 1, 2, 2, 3, 4}
segundo = [3, 4, 5]
# Creaión de un set en base a una lista. Set recibe un Iterable.
segundo = set(segundo)

primer | segundo 	# Unión. Y elimina duplicados
primer & segundo 	# Intersección. Y elimina duplicados
primer - segundo  # Diferencia {1, 2} Al de la izq le quito los de la dcha
primer ^ segundo  # Diferencia simétrica. Devuelve todos menos la intersección

# Los sets no están ordenados, por lo tanto no puedo hacer:
segundo[1]  # NO PUEDO, pero si puedo ver si un elemento está en el conjunto
if 5 in segundo:
    print("El 5 está")

# Diccionarios (pares llave-valor)
# Solo acepta strings como llave
punto = {"x": 25, "y": 50}
punto["x"]  # => 25
punto["y"]  # => 50
punto[0] 			# Error, porque no son listas
punto["z"] = 45		# Añado nueva llave dinámicamente
punto["t"]			# Error porque la llave no existe

if "t" in punto:
    punto["t"]		# Pregunto primero y me ahorro el error

punto.get("x")  		# => 25
punto.get("y")  		# => 50
punto.get("z")  		# => None
punto.get("z", 97)  	# => 97 Por defecto si no existe
del punto["x"]			# Elimina llave y valor
del (punto["y"])  		# También tengo una función "del"

for valor in punto:		# Iteramos las llaves
    print(valor, punto[valor])

for valor in punto.items():
    print(valor)		# Devuelve tuplas ('x', 25) ...

for llave, valor in punto.items():  # Desempaquetamos las tuplas
    print(llave, valor)		# Devuelve tuplas: x 25

usuarios = [
    {"id": 1, "nombre": "David"},
    {"id": 2, "nombre": "María"},
    {"id": 3, "nombre": "Begoña"},
    {"id": 4, "nombre": "Eladio"}
]

for usuario in usuarios:
    print(usuario["nombre"])

# Operador de desempaquetado
lista = [1, 2, 3, 4]
print(lista)  # => [1, 2, 3, 4]
print(1, 2, 3, 4)  # => 1 2 3 4
print(*lista)       # => 1 2 3 4 Desempaqueto la lista
# Para listas ...
lista2 = [5, 6]
combinada = [*lista, *lista2]  # => [1, 2, 3, 4, 5, 6]
# => ['Hola', 1, 2, 3, 4, 'mundo', 5, 6]
combinada = ["hola", *lista, "mundo", *lista2]

# Para diccionarios
punto1 = {"x": 19}
punto2 = {"y": 15}
nuevoPunto = {**punto1, **punto2}  # => {'x': 19, 'y': 15}
# => {'x': 19, 'y': 15, 'z': 'mundo'}
nuevoPunto = {**punto1, **punto2, "z": "mundo"}
# => {'x': 19, 't': 'tiempo', 'y': 15, 'z': 'mundo'}
nuevoPunto = {**punto1, "t": "tiempo", **punto2, "z": "mundo"}
# Nota: Se asigna de derecha a izquierda. Si la llave ya existe, se reasigna el valor.


# Filas (First in first out FIFO)
# Trabajar con LISTAS puede ser muy costoso computacionalmente si quito el elemento de la izquierda y
# desplazo todos los demás una posición a la izquierda. Para ello uso deque.
# Con 4 elemento puedo trabajar con listas, pero con 100.000.000 debo usar deque.

# from collections import deque
fila = deque([1, 2])
fila.append(3)
fila.append(4)
fila.append(5)
fila.popleft()  # => Quito elementos a la izquierda
if not fila:  # Falsy: lista vacía, string vacía o cero
    print("Fila vacía")

# Pilas (Last In First Out) Ej: Historial de navegación
# Se puede implementar con LISTAS
pila = []
pila.append(1)
pila.append(2)
pila.append(3)
pila.pop()  # => retorna el último elemento
pila[-1]  # => Acceder al último elemento de la lista
if not pila:    # Falsy: lista vacía, string vacía o cero
    print("Pila vacía")

# Ejercicio

# 1. Eliminar los espacios en blanco de un string
# y devolver una lista con los carateres restantes


def quita_espacios(texto):
    return list(texto.replace(" ", ""))

    # return [char for char in texto if char != " "]

# 2. Contar en un diccionario cuanto se repite los caracteres de un string


def cuenta_caracteres(lista):
    diccionario = {}

    for char in lista:
        if char in diccionario:
            diccionario[char] += 1
        else:
            diccionario[char] = 1
    return diccionario

# 3. Ordenar las llaves de un diccionario
# por el valor que tienen y devolver una lista
# que contiene tuplas [("a", 3), ("b", 4), etc..]


def ordena(diccionario):

    # # Ordenar un diccionario
    # return sorted(
    #     diccionario.items(),
    #     key=lambda key: key[1],
    # 	  reverse= True
    # )

    # Convertimos el diccionario a una matriz para poder ordenarla con sort
    matriz = []

    for item in diccionario:		# Iteramos las llaves
        matriz.append([item, diccionario[item]])

    # Ordenamos por el númeo de repeticiones
    matriz.sort(key=lambda el: el[1])

    # Convertimos un array de arrays en un array de tuplas
    tuplas = []
    for item in matriz:
        tuplas.append(tuple(item))

    # Devolvemos el array de tuplas
    return tuplas

# 4. De un listado de tuplas, devolver las tuplas que tenga el mayor valor


def mayores_tuplas(lista):
    tuplas = []
    valor = 0
    for tupla in lista:
        if tupla[1] > valor:
            tuplas.clear()
            tuplas.append(tupla)
            valor = tupla[1]
        elif tupla[1] == valor:
            tuplas.append(tupla)

    return tuplas


# 5. Crear un mensaje que diga:
# Los caracteres que más se repiten con 4 repeticiones son:
# -C
# -D

def mensaje_resumen(tuplas):
    repeticiones = tuplas[0][1]
    print(
        f"Los caracteres que más se repiten con {repeticiones} repeticiones son:")
    for tupla in tuplas:
        print(f"- {tupla[0].upper()}")


# 6. Juntar la solucion de los ejercicios anteriores
# para encontrar los caracteres que más se repiten
# de un sring

def caracteres_repetidos(string):
    lista = quita_espacios(string)
    diccionario = cuenta_caracteres(lista)
    tuplas = ordena(diccionario)
    tuplas_mayor = mayores_tuplas(tuplas)
    mensaje_resumen(tuplas_mayor)


caracteres_repetidos("aaaaaaEn un llugak lañsdf alksdfj asdf")


#############################
# Seccion 6: Clases en python
#############################

# Introducción a las clases
mensaje = "Hola mundo"
type(mensaje)

# Clase: es el plano de construcción
# Objeto: es una instancia de una clase

# Creando clases (PascalCase o UpperCamelCase)
# Así cuendo instancie no pongo como en otros lenguajes


class Perro:
    def habla(self):  # Esto ya no se llama función, es un método. Self es obligatorio
        print("Guay!")


mi_perro = Perro()  # Esto es como new Perro() en otros leguajes
type(mi_perro)      # Vemos a que clase pertenee
mi_perro.habla()    # No le paso ningún argumento
# Preguntamos si mi_perro es una instancia de Perro
isinstance(mi_perro, Perro)

# Constructor
# Es un método que se ejecuta siempre que se cree una instancia de la clase.


class Perro:
    # self hace referencia a la instancia creada, es decir "mi_perro"
    def __init__(self, nombre, edad):
        self.nombre = nombre    # Creación de ATRIBUTOS o PROPIEDAD
        self.edad = edad

    def habla(self):  # Esto ya no se llama función, es un método. Self es obligatorio
        print(f"{self.nombre} dice: Guau!")


mi_perro = Perro("Toby", 23)
print(mi_perro.nombre)

mi_perro2 = Perro("Felipe", 1)
print(mi_perro2.nombre)


# Propiedades de las clases
# Diferencia entre propiedades de clase y de instancia


class Perro:
    patas = 4  # Propiedad de la clase
    # self hace referencia a la instancia creada, es decir "mi_perro"

    def __init__(self, nombre, edad):
        self.nombre = nombre    # Creación PROPIEDAD de instancias (atributos)
        self.edad = edad        # Creación PROPIEDAD de instancias (atributos)

    def habla(self):  # Esto ya no se llama función, es un método. Self es obligatorio
        print(f"{self.nombre} dice: Guau!")


mi_perro = Perro("Toby", 3)
print(Perro.patas)  # => 4 Puedo acceder a través de la clase
print(mi_perro.patas)  # => 4
Perro.patas = 5
print(Perro.patas)  # => 5
print(mi_perro.patas)  # => 5
mi_perro.patas = 6
print(Perro.patas)  # => 5
print(mi_perro.patas)  # => 6
Perro.patas = 7
mi_perro2 = Perro("Jango", 5)
print(Perro.patas)  # => 7
print(mi_perro2.patas)  # => 7
print(mi_perro.patas)  # => 6 YA NO ES 7 PORQUE LO MODIFIQUE UNA VEZ


# Método de clase
# Usos:
# 1) Métodos en común para todas las intancias de la clase
# 2) Factory method para crear intancias de la clsae

class Perro:
    patas = 4

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    @classmethod
    def habla(cls):  # cls se refiere a la clase misma: Perro
        print("Guau!")

    @classmethod
    def factory(cls):  # Factory method. Crea instancias de perro
        return cls("Toby", 4)


perro3 = Perro.factory()


# Propiedades y métodos privados

class Perro:

    def __init__(self, nombre, edad):
        self.__nombre = nombre  # Propiedades privadas
        self.edad = edad

    def get_nombre(self):
        return self.__nombre

    # Encapsular la asignación de nombre en un método puede servir
    # para aplicar cierta lógica de negocio y evitar que se
    # asignen, por ejemplo un número negativo al nombre del perro
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def __habla(self):  # MÉTODO PRIVADO
        print(f"{self.__nombre} dice: Guau!")

    @classmethod
    def factory(cls):  # Factory method. Crea instancias de perro
        return cls("Toby", 4)


perro1 = Perro.factory()
print(perro1.habla())
print(perro1.__nombre)  # => error, atributo privado
print(perro1.get_nombre())

# Puedo hackear y ver las propiedades privadas de todas formas
# Pero no hay que hacerlo ya que si se ha declarado privado
# es porque el desarrollador lo ha estipulado así.
print(perro1.__dict__)
print(perro1._Perro__nombre)

# Decorador property

class Perro:

    def __init__(self, nombre, edad):
        self.nombre = nombre #Pasa por la validación del setter

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        if nombre.strip()
            self.__nombre = nombre
        return

perro = Perro("Toby")

# Métodos mágicos
# Se ejecuntan cuando no lo llamamos directamente
# __init__ es uno de ellos
# Todos comienzan y terminan con __
# Google: https://rszalski.github.io/magicmethods/ Representing your classes
# 
class Perro:
    def __init__(self, nombre, edad):
        self.nombre = nombre   
        self.edad = edad

    def __str__(self):
        return f"Clase Perro: {self.nombre}"

    def habla(self):  # Esto ya no se llama función, es un método. Self es obligatorio
        print(f"{self.nombre} dice: Guau!")


perro = Perro("Toby")
text = str(perro) #=> Llama a nuestro método mágico __str__

# Destructor
# Es un método mágico

class Perro:
    def __init__(self, nombre, edad):
        self.nombre = nombre   
        self.edad = edad

    def __del__(self):
        print(f"Chao peror :-( {self.nombre}")

    def __str__(self):
        return f"Clase Perro: {self.nombre}"

    def habla(self):  # Esto ya no se llama función, es un método. Self es obligatorio
        print(f"{self.nombre} dice: Guau!")


perro = Perro("Toby")
del perro

# Comparación de objetos

class Coordenadas:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon

    def __eq__(self, otro): #Otra instancia de la otra clase
        return self.lat == otro.lat and self.lon == otro.lon
    # Python es capaz de inferir el métod mágico __ne__ si ya tengo el __eq__
    
    
    # Con lo cual no es necesario ponerlo
    def __ne__(self, otro):
        return self.lat != otro.lat or self.lon != otro.lon
    # Python es capaz de inferir el métod mágico __ne__ si ya tengo el __eq__
    
    def __lt__(self, otro): # less than: coords < coords2) 
        return self.lat + self.lon < otro.lat + otro.lon
    # Python infiere automáticamente el coords > coords2

    def __le__(self, otro): #less or equal
        return self.lat + self.lon <= otro.lat + otro.lon
    # Python infiere automáticamente el coords >= coords2

    
coords = Coordenadas(45,27)
coords2 = Coordenadas(45, 27)
print(coords == coords2) # Sin método mágico __eq__
#=> False porque ocupan dos espacios en memoria diferentes. No son el mismo objeto
print(coords == coords2) # Con método mágico __eq__
# Cuando defino el método mágico __eq__, la cosa cambia

print(coords != coords2) # Con método mágico __eq__

print(coords < coords2) # Con método mágico __lt__

print(coords <= coords2) # Con método mágico __le__

# Contenedores: Meter objetos dentro de otros objetos

class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
    
    def __str__(self):
        return f"Producto {self.nombre} - Precio: {self.precio}"
        
    


class Categoria:
    productos = []
    def __init__(self, nombre, productos):
        self.nombre = nombre
        self.productos = productos
    
    def agregar(self, producto):
        self.productos.append(producto)

    def imprimir(self):
        for producto in self.productos:
            print(producto)

kayak = Producto("Kayak", 1000)
bicicleta = Producto("Bicicleta", 750)
surfboard = Producto("Surfboard", 500)
deportes = Categoria("Deporte", [kayak, bicicleta])

deportes.agregar(surfboard)

deportes.imprimir()


# Herencia
class Animal:
    def comer(self):
        print("comieno")

    
class Perro(Animal):
    def pasear(self):
        print("paseando")

perro = Perro()

class Chanchito(Perro): #Herencia multinivel. No hacerlo con más de 1 o 2 niveles
    
    def programar(self):
        print("programando")

# Herencia múltiple

class Animal:
    def comer(self):
        print("comieno")
    
    def pasear(self):
        print("paseando animales")

    
class Perro():
    def pasear(self):
        print("paseando al perro")


# Cuidado con el orden de herencia, del orden depende los métodos que se elijan
# en el caso de que estén repetidos. Se va de derecha a izquierda, quedándose con el 
# de más a la izquierda.
class Chanchito(Perro, Animal):
    
    def programar(self):
        print("programando")

chanchito = Chanchito()
chanchito.pasear() #=> "paseando al perro".
# Recoge los métodos de izquierda a derecha en función del orden
# en cómo se ha definido la herencia. Chanchito(Perro, Animal)
# Si la hubiera definido Chanchito(Animal, Perro) imprimiría
# "paseando animal"

# Anulación de método

class Ave:
    def __init__(self):
        self.volador = True

    def vuela(self):
        print("vuela ave")
    
class Pato(Ave):
    def __init__(self):
        super().__init__() # Ejecutamos el constructor de la clase padre
        self.nada = True
    
    def vuela(self):
        super().vuela()
        print("vuela pato")

# Ejemplo Real
# Principio de OMR System

class Model():
    tabla = False

    def __init__(self):
        if not self.tabla:
            print("Error, tienes que definir una tabla")

    def guardar(self):
        print(f"Guarando en {self.tabla} en BBDD")

    @classmethod  
    def buscar_por_id(self, _id): # Existe una función nativa en python llamada 'id' por eso pongo _
        print(f"Buscando por {_id} en la tabla {self.tabla}")


class Usuario(Model):
    tabla = "Usuario"

Usuario.buscar_por_id(123)

# Clases abstractas
# No se pueden instanciar y su origen es para ser heredables
# abc => abstrac class

#from abc import ABC, abstractmethod
class Model(ABC): #La hacemos abstracta
    
    # Ya no necesito el constructor, porque la clase Model no se puede
    # instanciar al ser abstracta

    # Creamos un método abstraco, que realmente es un propiedads
    @property
    @abstractmethod
    def tabla(self):
        pass
    
    @abstractmethod
    def guardar(self):
        pass

    @classmethod  
    def buscar_por_id(self, _id): # Existe una función nativa en python llamada 'id' por eso pongo _
        print(f"Buscando por {_id} en la tabla {self.tabla}")


class Usuario(Model):
    tabla = "Usuario"

    def guardar(self):
        print("guardando usuario")



# Poliformismo

#from abc import ABC, abstractmethod
class Model(ABC): #La hacemos abstracta
    @abstractmethod
    def guardar(self):
        pass

class Usuario(Model):
    def guardar(self):
        print("guardand en BBDD")

class Sesion(Model):
    def guardar(self):
        print("guardando en archivo")

def guardar(entidades):
    for entidad in entidades:
        entidad.guardar()

usuario = Usuario()
guardar(usuario) #=> guardando en base de datos

sesion = Sesion()
guardar(sesion) #=> guardando en archivo

guardar([sesion, usuario]) #=> POLIMORFISMO

# Duck typing

class Usuario():
    def guardar(self):
        print("guardand en BBDD")

class Sesion():
    def guardar(self):
        print("guardando en archivo")

# Esta función solo necesita que "entidades" sea una lista 
# y que cada elemento tenga el método "guardar"
# Como python tiene tipado dinámico, no comprueba que las 
# 'entidades' pasadas tengan el método "guardar"
# "si camina como un pato y suena como un pato, es un pato"
# no necesitamos implementar POLIMORFISMO de manera estricta
def guardar(entidades): 
    for entidad in entidades:
        entidad.guardar()


# Extendiendo tipos nativos
# Lo puedo hacer con los string, números, etc...

lista = list([1, 2, 3])
lista.append(4)
lista.insert(0,0)

class List(list): #Que extienda de list
    def prepend(self, item):
        self.insert(0, item)

lista = List([1, 3, 4])
lista.append(4)

lista.prepend(0)



#############################
# Seccion 7: Excepciones
#############################

# Introducción a las excepciones

try:
    n1 = int(input("Ingresa primer número"))
except:
    print("ocurrio un error :(")

# Tipos de excepciones
try:
    n1 = int(input("Ingresa primer número"))
except Exception as e:
    print(type(e))


try:
    n1 = int(input("Ingresa primer número"))
except ValueError as e:
    print("Ingrese un valor que correspona")

except NameError as e:
    print("Ocurrió un error")

# Else y finally

try:
    n1 = int(input("Ingresa primer número"))
except:
    print("ocurrio un error :(")

else: # Se ejecuta siempre y cuando no exista ningún error
    print("No ocurrió ningún error")

finally: # Se ejecuta siempre
    print("Se ejecuta siempre")


# Invocando excepciones
# https://docs.python.org/3/library/exceptions.html
# Final árbol con excepciones 
# No se deben lanzar excepciones muy seguidas porque son 
# costosas en rendimiento

def division(n=0):
    if n == 0:
        raise ZeroDivisionError("No se puede dividir por cero", f"{n}")
        
    return 5 / n

try: 
    division()
except ZeroDivisionError as e:
    print(e)

# Excepciones personalizadas
# Son útiles para agregar lógica o valores adicionales

class MiError(Exception):
    "Esta clase es para representar mi error. Documentación."

    def __init__(self, mensaje, codigo):
        self.mensaje = mensaje
        self.codigo = codigo
    
    # Personalizamos la salida de string cuando uso print(e)
    def __str__(self):
        return f"{self.mensaje} - codigo: {self.codigo}"


def division(n=0):
    if n == 0:
        raise MiError("No se puede dividir por cero", 805)
        
    return 5 / n

try: 
    division()

except MiError as e:
    print(e.codigo)
    print(e.mensaje)



#############################
# Seccion 8: Módulos
#############################

# Introducción

#usuarios_impuestos.py => convención de nombres
def guardar():
    print("guardando")

def pagar_impuestos():
    print("pagar impuestos")


#app.py
# from usuario import * => mala práctica
from usuario_impuestos import guardar, pagar_impuestos

guardar()
pargar_impuestos()

# Módulos compilados
# modulos/__pycache__
# Al imortar módulos, python crea carpetas sin darnos cuenta
# .pyc > (python caché) archivos compilados a bytecode
# Recompila en función de la fecha de creación


# Paquetes
# Módulo => apunta a archivos
# Paquetes => apunta a carpetas
# Para que python reconozca una carperta como módulo, debe contener
# un archivo llamado __init__.py

# Convenciones de importación
# from usuarios.acciones import guardar #=> bien
# guardar()

# from usuarios import acciones #=> bien
# acciones.guardar()

# import usuarios.acciones  # => tedioso
# usuarios.acciones.guardar()

# Sub paquetes
# Si dentro de los modulos, tengo submodulos, coloco nuevos __init__.py
# dentro de las carpetas y los referencio de la manera lógica

# Referenciando sub-paquetes anteriores
# from ..gestion.crud import guardar
# from ...usuaios import pagar  => subo un nivel más con un punto más

# Dir
import usuarios
print(dir(usuarios)) #=> puedo ver los subpaquetes de un paquete
# Sirve para crear frameworks
print(usuarios.__name__)
print(usuarios.__package__)
print(usuarios.__path__)
print(usuarios.__file__)

# Paquetes con nombres dinámicos
# Podemos ejecutarlo cuando se haya ejectuado el módulo de manera directa
if __name__ == "__main__":
    print("tarea de mantenimiento") 

# Import condicionados
if __name__ != "__main__":
    from ..gestion.crud.import guardar # Imports relativos
    from usuarios.gestion.crud.import guardar # Imports absolutos

if __name__ == "__main__":
    print("tarea de mantenimiento") 


#################################
# Seccion 9: Rutas y directorios
#################################

# Rutas
from pathlib import Path
Path(r"C:\Archivos de Programa\Minecraft")
Path("/usr/bin") #=> ruta absoluta
Path()
Path.home()
Path("one/__init__.py") #=> ruta relativa

path = Path("hola-mundo/mi-archivo.py")
path.is_file()
path.is_dir()
path.exists()

print(
    path.name,      #=> Nombre del archivo con extensión
    path.stem,      #=> Nombre del archivo sin extensión
    path.suffix,    #=> Extesión
    path.parent,    #=> hola-mundo
    path.absolute()
)

p = path.with_name("chanchito.py")  # Cambiamos el nombre del archivo
p = path.with_suffix(".bat")        # Cambio extensión
p = path.with_stem("feliz")         # Cambio nombre

# Diectorios
from pathlib import Path
path = Path("directorio")
path.exists()
path.mkdir()
path.rmdir()
path.rename("chanchito-feliz")

for p in path.interdir() #Para iterar un directorio
    print(p)

archivos = [p for p in path.interdir() if not p.is_dir()]
archivos = [p for p in path.glob("*.py")] # Solo archivos con extensión py
archivos = [p for p in path.glob("**/*.py")] # Solo archivos con extensión py y de todas las carpetas del árbol
archivos = [p for p in path.rglob("*.py")] #También recursivamente... Solo archivos con extensión py y de todas las carpetas del árbol


# Inyección de dependencias
import Correa

class Perro:
    def __init__(self):
        self.correa = Correa()

#### le inyecto dependencia

class Perro:
    def __init__(self, Correa):
        self.correa = Correa()

#### Inyección de funciones

### Sin inyección
import usuario
def guardar():
    usuario.guardar()


### Con inyección
def guardar(entidad):
    entidad.guardar()

# Ventajas: 
# 1) Reutilizar el código 
# 2) Desacoplar código
# 3) Más fácil escribir tests

def init_app(bbdd, api):
    #inicialización del módulo


# Import dinámico de paquetes
# Quiero importar todos los paquetes dentro de las carpetas de rutas
# Generamos una estructura de inyección de dependencias

from pathlib import Path

#Dependencias
import db
import graphql
import api

path = Path()
paths = [p for p in path.interdir() if p.is_dir()] 

dependencias = {
    "db": db,
    "api": api,
    "graphql": graphql
}

#Iteramos todos los path
def load(p):
    paquete = __import__(str(p).replace("/", "."))
    try:
        paquete.init(**dependencias)
    except:
        print("el paquete no tiene función init)")

list(map(load, paths)) #=> map: a un iterable le paso una función

# en modulo: dos/__init__.py
def init(db, api, **_):
    print(f"soy módulo dos {db} {api}")

# en modulo: uno/__init__.py
def init(graphql, **_):
    print(f"soy módulo uno {graphql} ")


#################################
# Seccion 10: Gestión de archivos
#################################

# Introducción

from pathlib import Path
from time import ctime
archivo = Path("archivos/archivo-prueba.txt")

archivo.exists()
archivo.rename()
archivo.unlink() # Eliminar archiv
archivo.stat() # Estadísticas del archivo
print("acceso", archivo.stat().st_atime) #acceso 1697299808.4961884
print("acceso", ctime(archivo.stat().st_atime)) # acceso Sat Oct 14 18:10:08 2023
print("creación", ctime(archivo.stat().st_ctime))
print("modificación", ctime(archivo.stat().st_mtime)) 

# Lectura y escritura
# Tomamos todo el contenido del arvhivo, lo manipulamos y lo volvemos a escribir
from pathlib import Path

archivo = Path("archivos/archivo-prueba.txt")
texto = archivo.read_text("utf-8").split("\n")
texto.insert(0, "Hola mundo")
archivo.write_text("\n".join(texto), "utf-8")

# Open
# Otra forma para trabajar con archivos
# escritura
from io import open
texto = "Hola mundo!"
archivo = open("archivos/hola-mundo.txt", "w") # Modo escritura.Si no existe python lo crea
archivo.write(texto)
archivo.close() # Cerrar para que no ocupe memoria en la máquina

# solo lectura
from io import open
archivo = open("archivos/hola-mundo.txt", "r") # Modo escritura.Si no existe python lo crea
texto = archivo.read()
archivo.close() # Cerrar para que no ocupe memoria en la máquina
print(texto)

# lectura como lista
archivo = open("archivos/hola-mundo.txt", "r") # Modo escritura.Si no existe python lo crea
texto = archivo.readlines() # Todas las líneas las deja en un listado
archivo.close() # Cerrar para que no ocupe memoria en la máquina
print(texto)

# with y seek
# métodos mágicos (with cierra los archivos automáticamente)
#__enter__  => se ejecuta al abrir
#__exit__ => se ejecuta al final del bloque
# No es necesario que llamemos a archivo.close()
with open("archivos/hola-mundo.txt", "r") as archivo:
    #print(archivo.readlines()) #=> carga todo el archivo en memoria
    for linea in archivo:      #=> carga de línea en línea
        print(linea)

    archivo.seek(0) #=> mueve el puntero de with open al CARÁCTER, no a la línea, del arvhivo que queramo del archivo

# Agregar cosas a un archivo 
archivo = open("archivos/hola-mundo.txt", "a+")
archivo.write("Chao mundo")
archivo.close()

# Lectura y escritura
with open("archivos/hola-mundo.txt", "r+") as archivo:
    texto = archivo.readlines() # Mueve el puntero hasta el final
    archivo.seek(0) # Muevo el puntero al principio
    texto[0] = "Chanchito feliz"
    archivo.writelines(texto)

# Archivos CSV
# Escritura
import csv
with open("archivos/archivo.csv", "w") as archivo:
    writer = csv.writer(archivo)
    writer.writerow(["twit_id", "user_id", "text"])
    writer.writerow([1000, 1, "Hola"])
    writer.writerow([1001, 2, "Adios"])

# Lectura
with open("archivos/archivo.csv") as archivo:
    reader = csv.reader(archivo)
    #print(list(reader))
    for linea in reader:
        print(linea)


# Actualizar
import os

with open("archivos/archivo.csv") as r, open("archivos/archivo_temp.csv", "w") as w:
    reader = csv.reader(r)
    writer = csv.writer(w)
    for linea in reader:
        if linea[0] == "1000":
            writer.writerow([1000, 1, "Texto modificado"])
        else:
            writer.writerow(linea)

os.remove("archivos/archivo.csv")
os.rename("archivos/archivo_temp.csv", "archivos/archivo.csv")


# Archivos JSON
# Crear
import json
from pathlib import Path
productos = [
    {"id": 1, "name": "Surfboard"},
    {"id": 2, "name": "Bicicleta"},
    {"id": 3, "name": "Skate"},
]

data = json.dumps(productos)
Path("archivos/productos.json").write_text(data)

# Leer json
data = Path("archivos/productos.json").read_text(encoding="utf-8")
productos = json.loads(data)
print(productos)

# Modificar json
productos[0]["name"] = "Chanchito feliz"
Path("archivos/productos.json").write_text(json.dumps(productos))

# Archivos comprimidos
from pathlib import Path
from zipfile import ZipFile

with ZipFile("archivos/comprimidos.zip", "w") as zip:
    for path in Path().rglob("*.*"): #Cualquier archivo que tenga cualquier nombre y cualquier extensión
        print(path)
        if str(path) != "archivos/comprimidos.zip":
            zip.write(path)

# Leer de archivos comprimidos
with ZipFile("archivos/comprimidos.zip") as zip:
    print(zip.namelist())
    info = zip.getinfo("archivos/06-comprimidos-py")
    print(
        info.file_size,
        info.compress_size
    )

    zip.extractall("archivos/descomprimidos")

###################################
# Seccion 11: Base de datos SQlite
###################################
# Creando conexión
import sqlite3 
con = sqlite3.connect("sqlite/app.db")
con.close() #Es necesario cerrar siempre para poder volver a guardar

# Creando tablas
import sqlite3 

con = sqlite3.connect("sqlite/app.db")
cursor = con.cursor()
cursor.execute(
    """
    CREATE TABLE if not exists usuarios
    (id INTEGER primary key, nombre VARCHAR(50));
    """
)
con.commit() # ¡Simpre!
con.close()  # Es necesario cerrar siempre para poder volver a guardar

# With (para no tener que poner siempre un commit y un close)
import sqlite3 

with sqlite3.connect("sqlite/app.db") as con:
    cursor = con.cursor()
    cursor.execute(
        """
        CREATE TABLE if not exists usuarios
        (id INTEGER primary key, nombre VARCHAR(50));
        """
    )
# with llama al metodo magico __exit__ que hace un commit y un close

# Insert evitando SQL Inyection
import sqlite3 

with sqlite3.connect("sqlite/app.db") as con:
    cursor = con.cursor()
    cursor.execute(
        "insert into usuarios values(?,?)",
        (1, "Hola mundo"),

    )
# Meto los valores con ? para evitar SQL Injection

# Insert many
import sqlite3 

with sqlite3.connect("sqlite/app.db") as con:
    cursor = con.cursor()
    usuarios = [
        (2, "Chanchito feliz"),
        (3, "Chanchito triste")
    ]
    cursor.executemany(
        "insert into usuarios values(?,?)",
        usuarios
    )

# Select one
import sqlite3 

with sqlite3.connect("sqlite/app.db") as con:
    cursor = con.cursor()
    cursor.execute("SELECT * from usuarios")
    print(cursor.fetchone())


# Select all

import sqlite3 

with sqlite3.connect("sqlite/app.db") as con:
    cursor = con.cursor()
    cursor.execute("SELECT * from usuarios")
    print(cursor.fetchall())



########################################
# Seccion 12: Paquetes nativos de Python
########################################

# Browser
# Integrar el navegador web desde Python
# Abrir el navegador con una url determinada tras un script de despliegue
import webbrowser
print("producto encontrado")
webbrowser.open("http://academia.holamundo.io")

# Fechas
import time
print(time.time()) # Cantidad de segundo desde 1 enero 1970 UTC

import datetime
fecha = datetime.datetime(2023, 1, 1)
print(fecha)

from datetime import datetime
fecha = datetime(2023, 1, 1)
fecha2 = datetime(2023, 2, 1)
ahora = datetime.now()
print(ahora)

# Fecha a partir de un string
fechaStr = datetime.strptime("2023-01-03", "%Y-%m-%d") # Con directives
# python 3 strptime directive en Google para ver todas las directivas
print(fechaStr)

# String a partir de una fecha
print(fecha.strftime("%y.%m.%d"))
print(fecha > fecha2) # Comparar
print(
    fecha.year,
    fecha.month,
    fecha.day,
    fecha.hour,
    fecha.minute
)

# Timedelta
# Timedelta me permita sumar o restar tiempo de manera práctica
from datetime import datetime, timedelta

fecha1 = datetime(2023,1,1) + timedelta(weeks=1)
fecha2 = datetime(2023,2,1)

delta = fecha2 - fecha1

print(delta)
print("dias", delta.days)
print("segundos", delta.seconds)
print("microsegundos", delta.microseconds)
print("total_seconds()", delta.total_seconds())

# Random
import random
import string

lista = [1, 2, 3, 4, 5, 6, 7, 8]
lista2 = [1, 2, 3, 4, 5, 6, 7, 8]
random.shuffle(lista) # Desordena la lista
print(
    random.random(),
    random.randint(1, 10), # Números entre 1 y 10
    lista,
    random.choice(lista2), # Escoge un elemento de la lista aleatoriamente
    random.choices(lista2, k=4),  # Escojo un conjunto
    random.choices("abcdefghi", k=4),  # También funciona con strings.
    # Puedo generar contraseñas aleatorias
    "".join(random.choices("abcdefghi", k=78))
)

# Para generar contraseñas, uso unas listas de strings ya predefinidas
# en la biblioteca strings
chars = string.ascii_letters
digitos = string.digits
seleccion = random.choices(chars + digitos, k=16)
print(seleccion)
contrasena = "".join(seleccion)
print(contrasena)

# Aplicaciones para la línea de comandos
# Ejemplo de aplicación para el renombrado de archivos
import os
from pathlib import Path
import sys


def cli(args):
    if len(args) == 1:
        print("No se pasaron argumentos")
        return
    if len(args) != 3:
        print("se necesitan 2 argumentos")
        return

    origen = args[1]
    o = Path(origen)
    if not o.exists():
        print("Origen no existe")
        return

    destino = args[2]
    d = Path(destino)
    if d.exists():
        print("El destino no puede existir")
        return
    
    os.rename(str(origen), str(destino))
    print("Archivo renombrado con éxito")

cli(sys.argv)

# Cómo enviar correos de texto plano
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText 
from email.mime.image import MIMEImage
from pathlib import Path
import smtplib

path = Path("modulos-nativos/holamundo.png") #Para adjuntar imágenes
mime_image = MIMEImage(path.read_bytes())
mensaje = MIMEMultipart()
mensaje["from"] = "Hola mundo"
mensaje["to"] = "ultimate@asde.es"
mensaje["subject"] = "Asunto"
cuerpo = MIMEText("Cuerpo del mensaje") # Texto plano
mensaje.attach(cuerpo)
mensaje.attach(mime_image)

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo() # Identificarnos con el servidor
    smtp.starttls() # Transport layer security. Envío de manera encriptada
    smtp.login("ultimate@ese.es", "holamundo123")
    smtp.send_message(mensaje)

# Enviar correos html con plantillas

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText #TEXTO PLANO
from email.mime.image import MIMEImage
from pathlib import Path
from string import Template
import smtplib

# plantilla = """ 
#     <b>Hola mundo! $usuario </b>
# """

#Puedo tener una plantilla en un archivo aparte
plantilla = Path("modulos-nativos/plantilla.html").read_text("utf-8")


template = Template(plantilla)
#cuerpo = template.substitute("usuario": "Chanchito feliz")
cuerpo = template.substitute(usuario="Chanchito feliz")



path = Path("modulos-nativos/holamundo.png") #Para adjuntar imágenes
mime_image = MIMEImage(path.read_bytes())
mensaje = MIMEMultipart()
mensaje["from"] = "Hola mundo"
mensaje["to"] = "ultimate@asde.es"
mensaje["subject"] = "Asunto"
cuerpo = MIMEText(cuerpo, "html") # HTML
mensaje.attach(cuerpo)
mensaje.attach(mime_image)

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo() # Identificarnos con el servidor
    smtp.starttls() # Transport layer security. Envío de manera encriptada
    smtp.login("ultimate@ese.es", "holamundo123")
    smtp.send_message(mensaje)



###########################################
# Seccion 13: Índice de paquetes en Python
###########################################
# Paquetes externos: Python package Index (web) Biblioteca gigante

#####################
# pip
####################

pip3 install requests
# En ubunte 23 me da problemas porque esta instalación se realiza con apt get install python3-requests
# Me recomienda crear ambientes virtuales

pip3 list # Todos los paquetes instalados

pip3 uninstall requests
pip3 install requests==2.18.1
pip3 install requests==2.18.* #Última versión compatible con la 2.18
pip3 install requests==2.* #Última versión compatible con la 2
#Si tengo instalado zsh, pongo comoillas => pip3 install 'requests==2.18.1' 

pip3 install requests~=2.18.1 # Con tilde elije la mejor que se parezca a lo pedido

import requests
r = requests.get("https://www.google.com.co")
print(r)

#############################
# Entornos virtuales
# Empaquetado de librerías
#############################

# En la carpeta que elija, escribo:
# Crea toda una estructura del intérprete de python con sus librerías
python3 -m venv env
 
# Para activar el entorno virtual tengo que ejectuar env/bin/activate
source env/bin/activate

# Desactivar ambiente virtual
deactivate

# Ahora en mi entorno puedo instalar y desintalar con pip3

#######################
# pipenv (venv + pip3)
#######################
pip3 install pipenv # Puede que en ubuntu 23: sudo apt-get install python3-pipenv

# una vez instalado pipenv
pipenv install requests # para instalar el paquete
# EN la carpeta del proyecto creará dos archivos pipfile y pipfile.lock
pipenv uninstall requests # Desinstala y actualiza pipefile


# ¿Dónde esta la carpeta env de antes?
pipenv --venv
# /home/david/.local/share/virtualenvs/package-LTdZVCTL
# Se hace así de manera práctica para liberar carga en nustro proyecto
# por si lo tenemos que compartir con otros desarrolladores

# Puedo seleccionar un intérprete u otro en VSCODE refrescando abajo el desplegable
# o también puedo teclear en la carpeta del proyecto
pipenv shell # para lanzar el ambiente virtual de la carpeta donde estoy
exit # para salir del ambiente virtual

# Pipfile
# Para instalar todas las dependencias definidas en pipfile
pipenv install
# Para instalar todas las dependencias definidas en pipfile.lock (versiones exactas)
pipenv install --ignore-pipfile
# Esta orden creará el ambiente y las dependencias requeridas


#######################
# pipenv graph : gestionando dependencias
#######################
pipenv graph
pipenv uninstall requests
pipenv graph # Sisguen estando las dependencias de requests

pipenv install requests==2.10.*

pipenv update --outdated # Lista todos los paquetes que pueden ser actualizados potencialmente
pipenv update # Actualiza todos
pipenv update requests # Actualiza solo el paquete requests

###############
# Documentando paquetes (creando mi primer paquete)
#######################

"""
Este es el módulo que incluyeer la clase del reproductor de música
"""

class Player:
    """
    Esta clase crea un reproducto de 
    música
    """

    def play(self, song):
        """
        Reproduce la canción que recibió
        en el constructor

        Parameters:
        song (str): este es un string con el path de la canción

        Returns:
        int: devuelve 1 si repoduce con éxito, en caso contrario devuelve 0
        """
        print("reproduciendo canción")

    def stop(self):
        print("stopping")

#######################
# Publicando paquetes
#######################

# Instalo globalmente
pip3 install setuptools wheel twine


# Choose a licence google
# Gnu gpl v3 => copy licence
# Creo dos archivos:
# LICENSE
# README.md

# setup.py
import setuptools
from pathlib import Path

long_dec = Path("README.md").read_text()

setuptools.setup(
    name="holamundoplayer",
    version="0.0.1",
    long_description=long_desc,
    packages=setuptools.find_packages(
        exclude=["mocks", "tests"]
    )
)

# Ejecuto: sdist source distribution
# bdist: build distribution
python3 setup.py sdist bdist_wheel

# Genera dos empaquetados "build" y "dist"
# La carpeta holamundoplayer.egg-info no nos interesa

# Subimos el paquete a pypi.org
twine upload dist/*


#######################
# Django
#######################
pipenv install django==4.1.7 # Instalo Django de manera encapsulada con todos los paquetes de Python
pipenv shell # Para activar este entorno


# Creamos un projecto Django (es como "rails new nombre-app") # EL "." es importante
django-admin startproject productly .

# Crea toda la estructura del proyecto
# Las carpetas productly/asgi.py y productly/wsgi.py los ingnoramos por el momento porque son estrategias de despliegue de la app
# __init__.py => para transformar la carpeta de productly en un PAQUETE
# settings.py
# urls.py => todas las rutas

python3 manage.py runserver # Enciendo el servidor

#! ESTO QUE SE VE ES UN PROYECTO. LOS PROYECTOS PUEDEN CONTENER MÚLTIPLES APLICACIONES !!

# Primera aplicación. ¿Cómo creo la primera aplicación en Django?
# Todas las aplicaciones pueden comunicarse entre sí. Son pequeñitas y reutilizables
python3 manage.py startapp productos # Se crea una nueva carpeta productos
#   Falta isntalar productos
#   Construir URLS /productos... 
#   Views: mapeo ruta / método / views

# Views
# Intalo productos, copio ProductosConfig en productly/settings.py
# Otras apps instaladas:
# 'django.contrib.admin', => permite ver los datos de base de datos
# 'django.contrib.auth',  => parte de regitro, login, etc

INSTALLED_APPS = [
    'django.contrib.admin', => permite ver los datos de base de datos
    'django.contrib.auth', => parte de regitro, login, etc
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'productos.apps.ProductosConfig', => Instalo mi aplicación


############
# URLS
###########


# Configuramos las urls: en productly/urls.py
# Primera ñapa, tengo que meter un 'include'
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('productos/', include('productos.urls')),
]

# En el paquete PRODUCTOS, creo urls.py
# Tengo que poner una variable urlpattersporquela función de include espera que tenga esa variable
from django.urls import path
from . import views #=> Significa que importo la view.py del paquete donde estoy, en este caso Productos

urlpatterns = [
    path('',views.index, name='index')
]


#######
# VIEWS
#######
# views.py
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

# /productos
def index(request):
    return HttpResponse('Hola Mundo!')



# Modelo

########
# Models
########

# productos/models.py
from django.db import models

# Create your models here.
class Categoria(models.Model):  # Hacemos que extienda de la clase Model
    nombre = models.CharField(max_length=255)

class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    stock = models.IntegerField()
    puntaje = models.FloatField()

    # CASCADE: elimina el producto
    # PROTECT: lanza un error
    # RESTRICT: solo elimina si no existen productos
    # SET_NULL: actualiza a valor nulo
    # SET_DEFAULT: asigna valor por defecto
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE) 

# Migraciones: Paso a paso de lo que se tiene que hacer para actualizar la base de datos
# Para que se puedan hacer las migraciones es necesario que tenga la aplicación PRODUCTOS
# isntalada en settings.py => 'productos.apps.ProductosConfig',
python3 manage.py makemigrations
# Genera un 0001_initial.py en migrations. Este archivo no lo tenemos que tocar. Lo gestiona todo
# python3 con "makemigrations"

# Aplicamos las migraciones
# La base de datos está en productly/db.squlite3 => lo veo con "DB Browser for SQLite"
python3 manage.py migrate

# Actualizar los modelos
# Añado en models.py =>    creado_en = models. DateTimeField(default=timezone.now) #Paso la referencia, no la fucnión
python3 manage.py makemigrations
python3 manage.py migrate

#Panel de administración
python3 manage.py createsuperuser

# Tenemos que registrar los modelos para que aparezcan en el panel de administraciónç
# en productos/admin.py
from django.contrib import admin
from .models import Categoria, Producto

# Register your models here.
admin.site.register(Categoria)
admin.site.register(Producto)

# Personalizando el administrador.
# En el listado de categorías, en el nombre aparece "Categoria object (1)"
# Si lo que queremos es que aparezca el nombre de la categoría voy a models
# y reescribo el método __str__

class Categoria(models.Model):  # Hacemos que extienda de la clase Model
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre

# Para personalizar lo que aparece en el panel de administrador tengo que crear un clase:
# admin.py
from django.contrib import admin
from .models import Categoria, Producto

class CategoriaAdmin(admin.ModelAdmin):
    # fields = ()  Campos que quiero que aparezcan en mi formulario
    # exclude= ()  Campos que NO quiero que aparezcan en mi formulario
    list_display = ('id', 'nombre') # Campos que aparecen en el listdo del index

class ProductoAdmin(admin.ModelAdmin):
    exclude = ('creado_en', )
    list_display = ('id', 'nombre', 'stock', 'creado_en')

# Register your models here.
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Producto, ProductoAdmin)

#########################################
# Interactuando con la base de datos

# En views.py
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Producto

# Create your views here.

# /productos
def index(request):
    
    # productos = Producto.objects.filter(puntaje__gte=5) #gte greated than or equal
    # productos = Producto.objects.filter(puntaje=3) #gte greated than or equal
    # producto = Producto.objects.get(id=1)
    # producto = Producto.objects.get(pk=1) lo mismo que id=1

    #productos = Producto.objects.all()
    #print(productos)
    #return HttpResponse(productos[0].nombre)
    
    #Este trabajo con Json no es recompendable. Habría que utilizar dependencia de terceros, pero para prototipado rápido me sirve
    productos = Producto.objects.all().values() # Values para que se pueda serializar
    return JsonResponse(list(productos), safe=False) # Json necesita un listado para poder funcionar y serializar el objeto

################
# Pylintrc
# Introduciendo plantillas HTML
En vscode me aparece en rojo Producto.objects, para solucionarlo tengo que instalar:  pipenv install pylint-djago
Creo en la raíz del proyecto un archivo .pylintrc con "load-plugins=pylint-django"
# En views.py
# /productos

def index(request):
    
    productos = Producto.objects.all()

    return render(
        request, 
        'index.html', # Esto lo creo en templates. Es una convención
        context={'productos': productos}
    )


    # Para trabajar con templates/index.html => EMMET. Nos permite escribir mucho código html 
    table.table>tr>thead>tr>th*4 y pulso enter. Magia

    # Instalando frameworks de CSS
    Boostrap

    # Compartiendo plantillas
    En settings, en la sección TEMPLATES
    TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',# Motor de templates
        'DIRS': [os.path.join(BASE_DIR, 'templates')], # Directorios donde se van a ir a buscar las plantillas
        'APP_DIRS': True, # Para buscar de manera automática en las carpetas de TEMPLATES de cada una de las aplicaciones que creemos
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug', # Cosas a las que podemos acceder dentro de la plantilla
                'django.template.context_processors.request', # Cosas a las que podemos acceder dentro de la plantilla
                'django.contrib.auth.context_processors.auth', # Cosas a las que podemos acceder dentro de la plantilla
                'django.contrib.messages.context_processors.messages', # Cosas a las que podemos acceder dentro de la plantilla
            ],
        },
    },
]
    EL BACKEND es el motor que interpreta los {%%} de los html

######################
## Parámetros URL


# En urls.py
urlpatterns = [
    path('',views.index, name='index'),
    path('<int:producto_id>',views.detalle, name='producto_detalle')
]

# En views.py
def detalle(request, producto_id):
    return HttpResponse(producto_id)


######################
## Obtener elementos
def detalle(request, producto_id):
    #return HttpResponse(producto_id)
    producto = Producto.objects.get(id=producto_id)
    
    return render(request, 'detalle.html',context={ 'producto': producto})


###############
## Excepciones

def detalle(request, producto_id):
    try:
        #return HttpResponse(producto_id)
        producto = Producto.objects.get(id=producto_id)

        return render(
            request, 
            'detalle.html',
            context={ 'producto': producto})
    except Producto.DoesNotExist:
        raise Http404()

# También puedo usar "get_object_or_404"


################
# Links
# En templates
  <a href="{% url 'productos:detalle' producto.id %}">
                    {{ producto.nombre }}
                </a>
            </td>
# En urls.py
app_name = 'productos' # De esta forma, en el nombre de los path no tengo que poner name='producto_index', 'producto_detalle'

urlpatterns = [
    path('',views.index, name='index'),
    path('<int:producto_id>',views.detalle, name='detalle')
]

####
# Formulaios en base a modelos
configurar en settings.py
INSTALLED_APPS = [
...
    'django.forms',
    'productos.apps.ProductosConfig',
]

# Creamos forms.py
from . import models
from django.forms import ModelForm

class ProductoForm(ModelForm):
    class Meta:
        model = models.Producto
        fields = ['nombre', 'stock', 'puntaje', 'categoria']

# Visualizando formularios


# Validando y guardando formularios
# novalidate
{% block content %}
<form novalidate action="{% url 'productos:formulario' %}" method='post'>
    {% csrf_token %}

# Personalizando formularios
en settings.py
import os
from pathlib import Path
from django.forms.renderers import TemplatesSetting

class CustomFormRenderer(TemplatesSetting):
    form_template_name = 'form_snippet.html'

FORM_RENDERER = "productly.settings.CustomFormRenderer"

###
# Agregando estilos

####
# Filtros personalizables
# Qué son las funciones lambdas
https://borjauria.es/que-son-y-como-utilizar-lambdas-en-python-4d1d168e2f90

# ¿Cómo usar los filtros en python
https://www.digitalocean.com/community/tutorials/how-to-use-the-python-filter-function-es
# la función "filter" devuelve un "iterador".. para convertirlo en list hay que aplicar "list"

###############
# Página de inicio

#urls.py
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('admin/', admin.site.urls),
    path('productos/', include('productos.urls')),
]

#views.py
from django.shortcuts import render

def inicio(request):
    return render(
        request,
        'inicio.html'
    )
#En "templates" añado inicio.html
{% extends "base.html" %}

{% block content %}
    Hola mundo! Bienvenidos a productly!

{% endblock %}

#########
# Barra de navegación



#####################
## ¿Cómo administrar multiples versiones de Python

https://www.freecodecamp.org/espanol/news/administrar-multiples-versiones-de-python-y-entornos-virtuales/

Múltiples versiones de Python: Diferentes instalaciones de Python en la misma máquina, por ejemplo, 2.7 y 3.4.

Necesito la 3.7.2

Entornos virtuales: entornos independientes aislados que pueden tener tanto una versión específica de Python como de cualesquiera paquetes específicos de proyecto instalados en ellos, sin afectar a otros proyecto

3 herramientas

venv  => Solo una versión de python con diferentes entornos virtuales. (pipenv = venv + pip3)
/ pyvenv => script obsoleto para multiples versiones de python


pyenv => múltiples versiones de python en 3.3+ con o sin entornos virtuales

pyenv-virtualenv => ython 2

#venv
Desde Python 3.3+ el paquete venv está incluido. Es ideal para crear entornos virtuales ligeros.

python3 -m venv nombre-del-directorio-a-crear => crea un entorno virtual
$ source nombre-dado/bin/activate => para activarlo
$ deactivate => para desactivarlo
$ rm -r nombre-dado => Eliminar por completo después de deactivarlo

Para indicar una versión:
$ python3.6 -m venv example-three-six

Cuando el entorno está activo, cualquier paquete puede ser instalado ahí mediante pip de manera normal
Se recomienda hacer esto para actualizar pip:
pip install --upgrade pip

requirements.txt especificando sus dependencias
pip install -r requirements.txt => instala las dependencias


#pyvenv => envoltorio venv, script obsoleto en 3.8
Hasta Python 3.6 un script llamado pyvenv también se incluyó como envoltorio de  venv, pero ya es obsoleto. Se eliminará por completo en Python 3.8.

#pyenv 
Instalar: https://github.com/pyenv/pyenv-installer

pyenv versions
python3 --version
pyenv install 3.7.2

Nota: Abro terminal
python3 --version
=> Python 3.11.4 (la global del sistema)

python --version 
=> error

Voy a carpeta Gauss con .python-version 3.7.2
python3 --version
=> Python 3.7.2 
python --version
=> Python 3.7.2 



# Para instalar Gauss:
pyenv install 3.7.17  => instalo la versions de python
pyenv virtualenv 3.7.17 gaussApp => creo un entorno virtual sobre la version
pyenv versions => veo todo, no es como rvm que tengo gemsets por separado
git clone https://github.com/jjmartinr01/gauss3.git gauss3
cd gauss
pyenv local gaussApp => al ejecutar en un directorio, activa la versión y crea .python-version
pip install -r requirements.txt


# Para célery añadir 
 importlib-metadata==4.13.0


pipenv shell # para lanzar el ambiente virtual de la carpeta donde estoy
pipenv --venv
# /home/david/.local/share/virtualenvs/package-LTdZVCTL



pip install -r requirements.txt => instala las dependencias
Me da problemas paho-mqtt
 > instalo: pip install --upgrade setuptools
y parece que me deja con un warning.Warning
Luego se isntalan más cosas, pero gracias al setuptools, lo solventa aunque haya errores


#Para poder entrar por admin http://127.0.0.1:8000/admin/
user: david
password: holahola

(gaussApp) david@lnx:/var/www/python/gauss3$ python3 manage.py createsuperuser
Nombre de usuario: david
Dirección de correo electrónico: david@gauss.es
Password: 
Password (again): 
Superuser created successfully.





#Instalación postgreSql
apt update
apt install postgresql postgresql-contrib
Crea un usuario postgrsql



ADMINITRACION BÁSICA DE USUARIOS
https://www.youtube.com/watch?v=8aN91vauy8o
#Acceder a postgres sin cambiar de cuenta
sudo -u postgres psql

#Acceder cambiando de cuenta
sudo su - postgres
psql

postgres=# \conninfo
You are connected to database "postgres" as user "postgres" via socket in "/var/run/postgresql" at port "5432".
postgres=# 

#Crear nuevo rol desde david
sudo -u postgres createuser --interactive

#Crear nuevo rol desde postgres
createuser --interactive

#NOTA createuser es un programa de PostgreSQl.. no de linux
He creado usuario gauss (no me ha pedido contraseña)

#Crear base de datos
# desde posgress account
createdb data_gauss3
#desde david account
sudo -u postgres createdb data_gauss3

GRANT ALL PRIVILEGES ON DATABASE data_gauss3 TO gauss;

# Me conecto como admin => a partir de la version 15, para que gauss pueda crear tablas en dta_gauss3
psql -h localhost -U postgres -d data_gauss3
GRANT ALL ON SCHEMA public TO gauss; 

# Tengo que indicarle desde el pront de linux "localhost" ..
# si no, trata de acceder con los sockets de linux y no deja.
psql -U gauss -h localhost
psql -U gauss -h localhost -d data_gauss3

data_gauss3=> \c
SSL connection (protocol: TLSv1.3, cipher: TLS_AES_256_GCM_SHA384, compression: off)
You are now connected to database "data_gauss3" as user "gauss".
\dt => "show tables"



\du => listar usuarios
\list => ver bases de datos


#Abrir una línea de commandos 












# Para sacar todos las librerias
pip freeze > requirements.txt

# Para célery añadir 
 importlib-metadata==4.13.0