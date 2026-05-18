"""
Proyecto logica: Katas de Python
Archivo unico con todos los ejercicios resueltos.

El objetivo es practicar:
- Tipos de datos basicos
- Estructuras de datos
- Condicionales
- Bucles
- Funciones
- Excepciones
- Clases
- Map, filter, reduce y lambda
- Buenas practicas

Nota: En el enunciado no aparece el ejercicio 35.
"""

from functools import reduce
import math


# ==================================================
# Ejercicio 1
# Escribe una función que reciba una cadena de texto como parámetro y devuelva un diccionario con las frecuencias
# de cada letra en la cadena. Los espacios no deben ser considerados.
# ==================================================

def frecuencia_letras(texto):
    """Devuelve un diccionario con la frecuencia de cada letra sin contar espacios."""
    frecuencias = {}

    for letra in texto:
        if letra != " ":
            letra = letra.lower()
            frecuencias[letra] = frecuencias.get(letra, 0) + 1

    return frecuencias


# ==================================================
# Ejercicio 2
# ==================================================

def doble_valores(numeros):
    """Devuelve una lista con el doble de cada valor usando map."""
    return list(map(lambda numero: numero * 2, numeros))


# ==================================================
# Ejercicio 3
# ==================================================

def palabras_con_objetivo(lista_palabras, palabra_objetivo):
    """Devuelve las palabras que contienen la palabra objetivo."""
    resultado = []

    for palabra in lista_palabras:
        if palabra_objetivo.lower() in palabra.lower():
            resultado.append(palabra)

    return resultado


# ==================================================
# Ejercicio 4
# ==================================================

def diferencia_listas(lista_1, lista_2):
    """Calcula la diferencia entre valores de dos listas usando map."""
    return list(map(lambda x, y: x - y, lista_1, lista_2))


# ==================================================
# Ejercicio 5
# ==================================================

def calcular_media_estado(notas, nota_aprobado=5):
    """Calcula la media y devuelve una tupla con media y estado."""
    if len(notas) == 0:
        return 0, "suspenso"

    media = sum(notas) / len(notas)

    if media >= nota_aprobado:
        estado = "aprobado"
    else:
        estado = "suspenso"

    return media, estado


# ==================================================
# Ejercicio 6
# ==================================================

def factorial(numero):
    """Calcula el factorial de un numero de forma recursiva."""
    if numero < 0:
        raise ValueError("El factorial no esta definido para numeros negativos")

    if numero == 0 or numero == 1:
        return 1

    return numero * factorial(numero - 1)


# ==================================================
# Ejercicio 7
# ==================================================

def tuplas_a_strings(lista_tuplas):
    """Convierte una lista de tuplas en una lista de strings usando map."""
    return list(map(lambda tupla: " ".join(map(str, tupla)), lista_tuplas))


# ==================================================
# Ejercicio 8
# ==================================================

def dividir_numeros(numero_1, numero_2):
    """Intenta dividir dos numeros controlando errores."""
    try:
        numero_1 = float(numero_1)
        numero_2 = float(numero_2)
        resultado = numero_1 / numero_2
        return f"Division exitosa. Resultado: {resultado}"
    except ValueError:
        return "Error: Debes introducir valores numericos."
    except ZeroDivisionError:
        return "Error: No se puede dividir entre cero."


def programa_division():
    """Programa interactivo para dividir dos numeros."""
    numero_1 = input("Introduce el primer numero: ")
    numero_2 = input("Introduce el segundo numero: ")
    print(dividir_numeros(numero_1, numero_2))


# ==================================================
# Ejercicio 9
# ==================================================

def filtrar_mascotas(mascotas):
    """Excluye mascotas prohibidas usando filter."""
    mascotas_prohibidas = ["Mapache", "Tigre", "Serpiente Piton", "Cocodrilo", "Oso"]

    return list(filter(lambda mascota: mascota not in mascotas_prohibidas, mascotas))


# ==================================================
# Ejercicio 10
# ==================================================

class ListaVaciaError(Exception):
    """Excepcion personalizada para listas vacias."""
    pass


def promedio_con_excepcion(numeros):
    """Calcula el promedio de una lista. Si esta vacia, lanza una excepcion."""
    if len(numeros) == 0:
        raise ListaVaciaError("La lista esta vacia. No se puede calcular el promedio.")

    return sum(numeros) / len(numeros)


def manejar_promedio(numeros):
    """Maneja la excepcion personalizada del promedio."""
    try:
        return promedio_con_excepcion(numeros)
    except ListaVaciaError as error:
        return str(error)


# ==================================================
# Ejercicio 11
# ==================================================

def validar_edad(edad):
    """Valida que la edad sea numerica y este entre 0 y 120."""
    try:
        edad = int(edad)

        if edad < 0 or edad > 120:
            raise ValueError("La edad debe estar entre 0 y 120.")

        return f"Edad valida: {edad}"
    except ValueError as error:
        return f"Error: {error}"


def programa_edad():
    """Programa interactivo para pedir edad al usuario."""
    edad = input("Introduce tu edad: ")
    print(validar_edad(edad))


# ==================================================
# Ejercicio 12
# ==================================================

def longitud_palabras(frase):
    """Devuelve una lista con la longitud de cada palabra usando map."""
    return list(map(len, frase.split()))


# ==================================================
# Ejercicio 13
# ==================================================

def letras_mayus_minus(caracteres):
    """Devuelve una lista de tuplas con cada letra en mayusculas y minusculas."""
    letras_unicas = sorted(set(caracteres))
    return list(map(lambda letra: (letra.upper(), letra.lower()), letras_unicas))


# ==================================================
# Ejercicio 14
# ==================================================

def palabras_por_letra(lista_palabras, letra):
    """Devuelve palabras que empiezan por una letra especifica usando filter."""
    return list(filter(lambda palabra: palabra.lower().startswith(letra.lower()), lista_palabras))


# ==================================================
# Ejercicio 15
# ==================================================

sumar_3_lista = lambda numeros: list(map(lambda numero: numero + 3, numeros))


# ==================================================
# Ejercicio 16
# ==================================================

def palabras_mas_largas(texto, n):
    """Devuelve palabras mas largas que n usando filter."""
    return list(filter(lambda palabra: len(palabra) > n, texto.split()))


# ==================================================
# Ejercicio 17
# ==================================================

def digitos_a_numero(digitos):
    """Convierte una lista de digitos en el numero correspondiente usando reduce."""
    return reduce(lambda acumulado, digito: acumulado * 10 + digito, digitos)


# ==================================================
# Ejercicio 18
# ==================================================

def estudiantes_sobresalientes(estudiantes):
    """Filtra estudiantes con calificacion mayor o igual a 90 usando filter."""
    return list(filter(lambda estudiante: estudiante["calificacion"] >= 90, estudiantes))


# ==================================================
# Ejercicio 19
# ==================================================

filtrar_impares = lambda numeros: list(filter(lambda numero: numero % 2 != 0, numeros))


# ==================================================
# Ejercicio 20
# ==================================================

def filtrar_enteros(lista):
    """Devuelve solo los valores de tipo int usando filter."""
    return list(filter(lambda elemento: type(elemento) == int, lista))


# ==================================================
# Ejercicio 21
# ==================================================

cubo = lambda numero: numero ** 3


# ==================================================
# Ejercicio 22
# ==================================================

def producto_total(numeros):
    """Calcula el producto total de una lista usando reduce."""
    return reduce(lambda x, y: x * y, numeros)


# ==================================================
# Ejercicio 23
# ==================================================

def concatenar_palabras(palabras):
    """Concatena una lista de palabras usando reduce."""
    return reduce(lambda x, y: x + " " + y, palabras)


# ==================================================
# Ejercicio 24
# ==================================================

def diferencia_total(numeros):
    """Calcula la diferencia total de los valores usando reduce."""
    return reduce(lambda x, y: x - y, numeros)


# ==================================================
# Ejercicio 25
# ==================================================

def contar_caracteres(texto):
    """Cuenta el numero de caracteres de una cadena."""
    return len(texto)


# ==================================================
# Ejercicio 26
# ==================================================

resto_division = lambda numero_1, numero_2: numero_1 % numero_2


# ==================================================
# Ejercicio 27
# ==================================================

def promedio(numeros):
    """Calcula el promedio de una lista de numeros."""
    if len(numeros) == 0:
        return 0

    return sum(numeros) / len(numeros)


# ==================================================
# Ejercicio 28
# ==================================================

def primer_duplicado(lista):
    """Devuelve el primer elemento duplicado de una lista."""
    vistos = set()

    for elemento in lista:
        if elemento in vistos:
            return elemento
        vistos.add(elemento)

    return None


# ==================================================
# Ejercicio 29
# ==================================================

def enmascarar_variable(variable):
    """Convierte una variable a string y enmascara todo excepto los ultimos 4 caracteres."""
    texto = str(variable)

    if len(texto) <= 4:
        return texto

    return "#" * (len(texto) - 4) + texto[-4:]


# ==================================================
# Ejercicio 30
# ==================================================

def son_anagramas(palabra_1, palabra_2):
    """Determina si dos palabras son anagramas."""
    palabra_1 = palabra_1.lower().replace(" ", "")
    palabra_2 = palabra_2.lower().replace(" ", "")

    if palabra_1 == palabra_2:
        return False

    return sorted(palabra_1) == sorted(palabra_2)


# ==================================================
# Ejercicio 31
# ==================================================

class NombreNoEncontradoError(Exception):
    """Excepcion para nombres no encontrados."""
    pass


def buscar_nombre(lista_nombres, nombre_buscado):
    """Busca un nombre en una lista. Si no esta, lanza una excepcion."""
    if nombre_buscado in lista_nombres:
        return f"{nombre_buscado} fue encontrado."

    raise NombreNoEncontradoError(f"{nombre_buscado} no fue encontrado.")


def programa_buscar_nombre():
    """Programa interactivo para buscar un nombre."""
    nombres = input("Introduce nombres separados por coma: ").split(",")
    nombres = [nombre.strip() for nombre in nombres]
    nombre_buscado = input("Introduce el nombre que quieres buscar: ").strip()

    try:
        print(buscar_nombre(nombres, nombre_buscado))
    except NombreNoEncontradoError as error:
        print(error)


# ==================================================
# Ejercicio 32
# ==================================================

def buscar_puesto(nombre_completo, empleados):
    """Busca el puesto de un empleado por nombre completo."""
    for empleado in empleados:
        if empleado["nombre_completo"].lower() == nombre_completo.lower():
            return empleado["puesto"]

    return "La persona no trabaja aqui."


# ==================================================
# Ejercicio 33
# ==================================================

sumar_listas = lambda lista_1, lista_2: list(map(lambda x, y: x + y, lista_1, lista_2))


# ==================================================
# Ejercicio 34
# ==================================================

class Arbol:
    """Representa un arbol con tronco y ramas."""

    def __init__(self):
        self.tronco = 1
        self.ramas = []

    def crecer_tronco(self):
        """Aumenta la longitud del tronco en una unidad."""
        self.tronco += 1

    def nueva_rama(self):
        """Agrega una nueva rama de longitud 1."""
        self.ramas.append(1)

    def crecer_ramas(self):
        """Aumenta en una unidad la longitud de todas las ramas."""
        self.ramas = [rama + 1 for rama in self.ramas]

    def quitar_rama(self, posicion):
        """Elimina una rama en una posicion especifica."""
        if posicion < 0 or posicion >= len(self.ramas):
            raise IndexError("La posicion de la rama no existe.")

        self.ramas.pop(posicion)

    def info_arbol(self):
        """Devuelve informacion sobre el arbol."""
        return {
            "longitud_tronco": self.tronco,
            "numero_ramas": len(self.ramas),
            "longitudes_ramas": self.ramas
        }


# ==================================================
# Ejercicio 35
# ==================================================
# El enunciado proporcionado no incluye ejercicio 35.


# ==================================================
# Ejercicio 36
# ==================================================

class UsuarioBanco:
    """Representa a un usuario de un banco."""

    def __init__(self, nombre, saldo, cuenta_corriente):
        self.nombre = nombre
        self.saldo = saldo
        self.cuenta_corriente = cuenta_corriente

    def retirar_dinero(self, cantidad):
        """Retira dinero del saldo del usuario."""
        if not self.cuenta_corriente:
            raise ValueError("El usuario no tiene cuenta corriente.")

        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor que cero.")

        if cantidad > self.saldo:
            raise ValueError("Saldo insuficiente.")

        self.saldo -= cantidad

    def transferir_dinero(self, otro_usuario, cantidad):
        """Transfiere dinero desde otro usuario al usuario actual."""
        if not self.cuenta_corriente or not otro_usuario.cuenta_corriente:
            raise ValueError("Ambos usuarios deben tener cuenta corriente.")

        otro_usuario.retirar_dinero(cantidad)
        self.saldo += cantidad

    def agregar_dinero(self, cantidad):
        """Agrega dinero al saldo del usuario."""
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor que cero.")

        self.saldo += cantidad

    def mostrar_info(self):
        """Devuelve la informacion del usuario."""
        return {
            "nombre": self.nombre,
            "saldo": self.saldo,
            "cuenta_corriente": self.cuenta_corriente
        }


# ==================================================
# Ejercicio 37
# ==================================================

def contar_palabras(texto):
    """Cuenta cuantas veces aparece cada palabra en un texto."""
    palabras = texto.lower().split()
    conteo = {}

    for palabra in palabras:
        conteo[palabra] = conteo.get(palabra, 0) + 1

    return conteo


def reemplazar_palabras(texto, palabra_original, palabra_nueva):
    """Reemplaza una palabra por otra."""
    return texto.replace(palabra_original, palabra_nueva)


def eliminar_palabra(texto, palabra_eliminar):
    """Elimina una palabra del texto."""
    palabras = texto.split()
    palabras_filtradas = [palabra for palabra in palabras if palabra != palabra_eliminar]
    return " ".join(palabras_filtradas)


def procesar_texto(texto, opcion, *args):
    """Procesa un texto segun la opcion indicada."""
    if opcion == "contar":
        return contar_palabras(texto)

    if opcion == "reemplazar":
        if len(args) != 2:
            raise ValueError("Para reemplazar debes indicar palabra_original y palabra_nueva.")
        return reemplazar_palabras(texto, args[0], args[1])

    if opcion == "eliminar":
        if len(args) != 1:
            raise ValueError("Para eliminar debes indicar una palabra.")
        return eliminar_palabra(texto, args[0])

    raise ValueError("Opcion no valida. Usa contar, reemplazar o eliminar.")


# ==================================================
# Ejercicio 38
# ==================================================

def momento_del_dia(hora):
    """Indica si es de noche, de dia o de tarde segun la hora."""
    if hora < 0 or hora > 23:
        return "Hora no valida."

    if 6 <= hora < 12:
        return "Es de dia."

    if 12 <= hora < 20:
        return "Es de tarde."

    return "Es de noche."


def programa_momento_dia():
    """Programa interactivo para indicar momento del dia."""
    try:
        hora = int(input("Introduce una hora entre 0 y 23: "))
        print(momento_del_dia(hora))
    except ValueError:
        print("Error: Debes introducir un numero entero.")


# ==================================================
# Ejercicio 39
# ==================================================

def calificacion_texto(nota):
    """Devuelve la calificacion en texto segun una nota numerica."""
    if nota < 0 or nota > 100:
        return "Nota no valida."

    if nota <= 69:
        return "insuficiente"

    if nota <= 79:
        return "bien"

    if nota <= 89:
        return "muy bien"

    return "excelente"


# ==================================================
# Ejercicio 40
# ==================================================

def calcular_area(figura, datos):
    """Calcula el area de rectangulo, circulo o triangulo."""
    figura = figura.lower()

    if figura == "rectangulo":
        base, altura = datos
        return base * altura

    if figura == "circulo":
        radio = datos[0]
        return math.pi * radio ** 2

    if figura == "triangulo":
        base, altura = datos
        return (base * altura) / 2

    raise ValueError("Figura no valida. Usa rectangulo, circulo o triangulo.")


# ==================================================
# Ejercicio 41
# ==================================================

def calcular_precio_final(precio_original, tiene_cupon, valor_cupon=0):
    """Calcula el precio final despues de aplicar un descuento."""
    if precio_original < 0:
        raise ValueError("El precio original no puede ser negativo.")

    if tiene_cupon:
        if valor_cupon > 0:
            precio_final = precio_original - valor_cupon

            if precio_final < 0:
                precio_final = 0

            return precio_final

        return precio_original

    return precio_original


def programa_compra():
    """Programa interactivo para calcular precio final de una compra."""
    try:
        precio_original = float(input("Introduce el precio original: "))
        respuesta = input("Tienes cupon de descuento? si/no: ").lower()

        if respuesta == "si":
            valor_cupon = float(input("Introduce el valor del cupon: "))
            precio_final = calcular_precio_final(precio_original, True, valor_cupon)
        else:
            precio_final = calcular_precio_final(precio_original, False)

        print(f"El precio final es: {precio_final}")
    except ValueError as error:
        print(f"Error: {error}")


# ==================================================
# Pruebas automaticas para terminal
# ==================================================

def imprimir_titulo(numero, descripcion):
    """Imprime un titulo ordenado para cada ejercicio."""
    print("\n" + "=" * 60)
    print(f"EJERCICIO {numero}: {descripcion}")
    print("=" * 60)


def ejecutar_pruebas():
    """Ejecuta pruebas de todos los ejercicios sin pedir input al usuario."""

    imprimir_titulo(1, "Frecuencia de letras")
    print(frecuencia_letras("Hola mundo"))

    imprimir_titulo(2, "Doble de valores con map")
    print(doble_valores([1, 2, 3, 4]))

    imprimir_titulo(3, "Buscar palabras que contienen una palabra objetivo")
    print(palabras_con_objetivo(["casa", "casita", "perro", "casona"], "casa"))

    imprimir_titulo(4, "Diferencia entre dos listas con map")
    print(diferencia_listas([10, 20, 30], [1, 2, 3]))

    imprimir_titulo(5, "Media y estado")
    print(calcular_media_estado([7, 8, 6, 9]))

    imprimir_titulo(6, "Factorial recursivo")
    print(factorial(5))

    imprimir_titulo(7, "Tuplas a strings con map")
    print(tuplas_a_strings([("Hola", "mundo"), ("Python", 3)]))

    imprimir_titulo(8, "Division con manejo de errores")
    print(dividir_numeros(10, 2))
    print(dividir_numeros(10, 0))
    print(dividir_numeros("hola", 2))

    imprimir_titulo(9, "Filtrar mascotas prohibidas")
    print(filtrar_mascotas(["Perro", "Gato", "Tigre", "Oso", "Canario"]))

    imprimir_titulo(10, "Promedio con excepcion personalizada")
    print(manejar_promedio([5, 7, 9]))
    print(manejar_promedio([]))

    imprimir_titulo(11, "Validar edad")
    print(validar_edad("25"))
    print(validar_edad("abc"))
    print(validar_edad("150"))

    imprimir_titulo(12, "Longitud de palabras con map")
    print(longitud_palabras("Estoy aprendiendo Python"))

    imprimir_titulo(13, "Letras en mayusculas y minusculas")
    print(letras_mayus_minus("python"))

    imprimir_titulo(14, "Palabras que empiezan por una letra")
    print(palabras_por_letra(["mesa", "manzana", "perro", "mono"], "m"))

    imprimir_titulo(15, "Lambda que suma 3")
    print(sumar_3_lista([1, 2, 3]))

    imprimir_titulo(16, "Palabras mas largas que n")
    print(palabras_mas_largas("Python es un lenguaje muy interesante", 4))

    imprimir_titulo(17, "Digitos a numero con reduce")
    print(digitos_a_numero([5, 7, 2]))

    imprimir_titulo(18, "Estudiantes con calificacion >= 90")
    estudiantes = [
        {"nombre": "Ana", "edad": 20, "calificacion": 95},
        {"nombre": "Luis", "edad": 21, "calificacion": 82},
        {"nombre": "Marta", "edad": 22, "calificacion": 90}
    ]
    print(estudiantes_sobresalientes(estudiantes))

    imprimir_titulo(19, "Lambda para filtrar impares")
    print(filtrar_impares([1, 2, 3, 4, 5, 6]))

    imprimir_titulo(20, "Filtrar solo enteros")
    print(filtrar_enteros([1, "hola", 3, "python", 5]))

    imprimir_titulo(21, "Cubo con lambda")
    print(cubo(3))

    imprimir_titulo(22, "Producto total con reduce")
    print(producto_total([2, 3, 4]))

    imprimir_titulo(23, "Concatenar palabras con reduce")
    print(concatenar_palabras(["Hola", "mundo", "Python"]))

    imprimir_titulo(24, "Diferencia total con reduce")
    print(diferencia_total([100, 20, 10]))

    imprimir_titulo(25, "Contar caracteres")
    print(contar_caracteres("Hola mundo"))

    imprimir_titulo(26, "Resto de division con lambda")
    print(resto_division(10, 3))

    imprimir_titulo(27, "Promedio")
    print(promedio([10, 20, 30]))

    imprimir_titulo(28, "Primer duplicado")
    print(primer_duplicado([1, 2, 3, 2, 4]))

    imprimir_titulo(29, "Enmascarar variable")
    print(enmascarar_variable("123456789"))

    imprimir_titulo(30, "Anagramas")
    print(son_anagramas("roma", "amor"))

    imprimir_titulo(31, "Buscar nombre con excepcion")
    try:
        print(buscar_nombre(["Ana", "Luis", "Marta"], "Luis"))
        print(buscar_nombre(["Ana", "Luis", "Marta"], "Pedro"))
    except NombreNoEncontradoError as error:
        print(error)

    imprimir_titulo(32, "Buscar puesto de empleado")
    empleados = [
        {"nombre_completo": "Ana Garcia", "puesto": "Analista"},
        {"nombre_completo": "Luis Perez", "puesto": "Desarrollador"}
    ]
    print(buscar_puesto("Ana Garcia", empleados))
    print(buscar_puesto("Pedro Lopez", empleados))

    imprimir_titulo(33, "Sumar listas con lambda")
    print(sumar_listas([1, 2, 3], [4, 5, 6]))

    imprimir_titulo(34, "Clase Arbol")
    arbol = Arbol()
    arbol.crecer_tronco()
    arbol.nueva_rama()
    arbol.crecer_ramas()
    arbol.nueva_rama()
    arbol.nueva_rama()
    arbol.quitar_rama(1)
    print(arbol.info_arbol())

    imprimir_titulo(35, "No aparece en el enunciado")
    print("El enunciado proporcionado no incluye ejercicio 35.")

    imprimir_titulo(36, "Clase UsuarioBanco")
    alicia = UsuarioBanco("Alicia", 100, True)
    bob = UsuarioBanco("Bob", 50, True)
    bob.agregar_dinero(20)

    try:
        alicia.transferir_dinero(bob, 80)
    except ValueError as error:
        print(f"No se pudo transferir 80 desde Bob a Alicia: {error}")

    alicia.retirar_dinero(50)
    print(alicia.mostrar_info())
    print(bob.mostrar_info())

    imprimir_titulo(37, "Procesar texto")
    texto = "python es facil python es util"
    print(procesar_texto(texto, "contar"))
    print(procesar_texto(texto, "reemplazar", "python", "SQL"))
    print(procesar_texto(texto, "eliminar", "es"))

    imprimir_titulo(38, "Momento del dia")
    print(momento_del_dia(9))
    print(momento_del_dia(16))
    print(momento_del_dia(23))

    imprimir_titulo(39, "Calificacion en texto")
    print(calificacion_texto(65))
    print(calificacion_texto(75))
    print(calificacion_texto(85))
    print(calificacion_texto(95))

    imprimir_titulo(40, "Calcular area")
    print(calcular_area("rectangulo", (5, 3)))
    print(round(calcular_area("circulo", (4,)), 2))
    print(calcular_area("triangulo", (6, 2)))

    imprimir_titulo(41, "Precio final con descuento")
    print(calcular_precio_final(100, True, 15))
    print(calcular_precio_final(100, False))


if __name__ == "__main__":
    ejecutar_pruebas()