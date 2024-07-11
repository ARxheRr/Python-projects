print("hola mundo")
x = 5
print(x)

#suma
a = 3
b = 7 

print( a + b)

#Condicional
a = 10 
if a == 10: 
    print("Es 10")
else: 
    print("No es 10")


Valor_Decimal = 10.3234
mi_cadena = "hola mundo"

#Cadenas y operadores aritmeticos

x = "El valor de (a + b) * c es"

a, b, c = 4, 3, 2

d = (a + b) * c

imprimir = True

if imprimir:
    print (x, d)
  
'''
Esto es un comentario
de varias líneas
de código
'''

#identacion de bloques de codigo

if True:
    print(True)

x = 5
y = 10

x = 5; y = 10

#MULTIPLES LINEAS
x = 1 + 2 + 3 + 4 + \
     5 + 6 + 7 + 8 

x = (1 + 2 + 3 + 4 + 
     5 + 6 + 7 + 8 )

def funcion( a, b, c): 
    return a + b + c

d = funcion(10, 23,
             3)

#Creando variables

x = y = z = 10

x, y = 4, 2

x, y, z = 1, 2, 3

#Nombre variables
'''
Por otro lado existen ciertas normas a la hora de nombrar variables:

El nombre no puede empezar por un número
No se permite el uso de guiones -
Tampoco se permite el uso de espacios.
Se muestran unos ejemplos de nombres de variables válidos y no válidos.
'''

#Valido 
_variable = 10
vari_able = 10
variable10 = 10
variable = 60
variaBle = 10

#No valido
'''
2variable = 10
var-iable = 10
var iable = 10
No utilizar palabras reservadas
'''

#Uso de parentesis
x = 10
y = x*3-3**10-2+3

y  = 10
y = (x*3-3)**(10-2)+3

#Variables y alcance

x = 10

def function():
    x = 5

function()
print(x)

print("Esto es el contennido a imprimir")

x = 10
print( x )

x = 10
y = 20
print("Los valores x, y son:", x, y)

#CONDICIONALES

lenguaje =  "Python"

if lenguaje == "Python" :
    print("Estoy de acuerdo, python es el mejor")
elif lenguaje == "java":
    print("No me gusta, java no mola")
else:
    print("Ninguno otro lenguaje supera python")

#Bucles while, for, break, continue

x = 0
while x < 3:
    print(x)
    x += 1

for i in range(3):
    print(i)

for i in range(3):
    if i == 1:
        continue
    print(i)

x = 0
while True:
    print(x)
    if x == 2:
       break
    x += 1

#Valores FAlSE, TRUE, NONE

x = (5 == 1)
print(x)

x = True
if x:
    print("Python")

#none se retorna cuando una funcion no cuenta con return
def mi_funcion():
    pass
print(mi_funcion())

#Operadores logicos and, or, not

print(True and False)
print( True or False)
print(not True)

#Funciones def, return, lambda, pass, yield 
def funcion_suma(a, b):
    print("La suma es:", a + b)
funcion_suma( 10, 3)

def funcion_suma(a, b):
    return a + b

suma = funcion_suma( 10, 3)
print("La suma es igual ", suma)

print("La suma es",(lambda a, b: a + b )(3, 5))

def funcion_suma(a, b):
    pass

def generardor():
    n = 1
    yield n

    n += 1
    yield n

    n += 1
    yield n

for i in generardor():
    print(i)  


###Clases####
class miClase:
    def __init__(self):
        print("Creando un objeto de MiClase")
Objeto = miClase()



##Excepciones assert, try, except, finally, raise
x = 10
valor = None
try:
    valor = int(x)
except Exception as e:
    print("Hubo un error: ", e)
finally:
    print("El error es: ", valor)

##Variables globales##
a = 0 

def suma_uno():
    global a
    a = a + 1

suma_uno()
print(a)

def funcion_a():
    x = 10

    def funcion_b():
        nonlocal x
        x = 20
        print("funcion_b", x)

    funcion_b()
    print("funcion_a", x)


funcion_a()

#####MODULOS from, Import

from collections import  namedtuple

##### Pertenencia e identidad in, is

lista = ["a","b","c",]
print("a" in lista) # se encuentra en la lista

a = [1,2]
b = [1,2]
c = a

print(a is b)
print(a is c)

##Eliminar variables
a = 10
#del a
print(a)

###Context manager: with, as esto se volvio comentario porque ejecuta una llmada a un fichero y esta no se especifica unicamente es para conocer que pertenecen a un cotexto
'''
with open('fichero.txt', 'r') as file:
    print(file.read())
'''
##Concurrencia async, await

import asyncio

async def proceso(id_proceso):
    print("Empieza proceso:", id_proceso)
    await asyncio.sleep(10)
    print("Acaba proceso:", id_proceso)

async def main():
    await asyncio.gather(proceso(1), proceso(2), proceso(3))

asyncio.run(main())


## Duck in Typing en python / Tipado dinamico
class Pato:
    def hablar(self):
        print("¡Cuan!, Cua!")

p = Pato()

p.hablar()

def llamar_hablar(x):
    x.hablar()

class Perro:
    def hablar(self):
        print("¡Guau, Gua!")

class Gato:
    def hablar(self):
        print("¡Miau, Miau!")

class Vaca:
    def hablar(hablar):
        print("¡Muuu, Muuu!")

llamar_hablar(Perro())
llamar_hablar(Gato())
llamar_hablar(Vaca())

lista = [Perro(), Gato(), Vaca()]

for animal in lista:
    animal.hablar()


class Foo():
    def __len__(self):
        return 99

class Bar():
    pass



##Unpacking en python 

a, b, c = [1, 2, 3]

print(a)
print(b)
print(c)


a, b, c = (1, 2, 3)

print(a)
print(b)
print(c)

a, b, c = "123"

print(a)
print(b)
print(c)

a, b, c = {'uno': 1, 'dos':2, 'tres': 3}
print(a) # uno
print(b) # dos
print(c) # tres

a, b, c = range(3)
print(a) # 1
print(b) # 2
print(c) # 3

*a, b = (1, 2, 3)
print(a) # [1, 2]
print(b) # 3

a, *b = (1, 2, 3)
print(a) # 1
print(b) # [2, 3]

a = [1, 2]
b = [3, 4]
c = [*a, *b]

print(c)
# [1, 2, 3, 4]

a = {"uno": 1, "dos": 2}
b = {"tres": 3, "cuatro": 4}

c = {**a, **b}

print(c)
# {'uno': 1, 'dos': 2, 'tres': 3, 'cuatro': 4}

a = {"uno": 1, "dos": 2}
b = {"uno": 0, "dos": 0}

c = {**a, **b}

print(c)
# {'uno': 0, 'dos': 0}

for primero, *resto in [(1, 2, 3), (4, 5, 6, 7)]:
    print("Primero:", primero)
    print("Resto:", resto)
    
# Primero: 1
# Resto: [2, 3]
# Primero: 4
# Resto: [5, 6, 7]

a, b = (1, 2)
print(a, b)
# 1 2

a, b = b, a
print(a, b)
# 2 1

def funcion(a, *args, **kwargs):
    print(f"args={a} args={args} kwargs={kwargs}")

funcion(1)
# args=1 args=() kwargs={}

funcion(1, 2)
# args=1 args=(2,) kwargs={}

funcion(1, 2, 3, cuatro=4, cinco=5)
# args=1 args=(2, 3) kwargs={'cuatro': 4, 'cinco': 5}