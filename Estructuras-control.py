#condicional if
a = 4
b = 2
if b != 0:
    print(a/b)

if b != 0:
    c = a/b
    print("Dentro de if")
print("Fuera de if")

if b > 0:
    print(a/b)

if a > 5 and a <15:
    print ("Mayor a 5 y menor que 15")

#if a > 5 : #Esto genera un error


if a > 5:
    pass #Mejor dejarlo asi 

if a > 5:print("Es >  5") # esto  no es muy recomendable pero se puede 

if a> 5: print("Es > 5"); print ("Esto es dentro del if") #Esto es valido si el bloque de codigo no es muy largo

#Uso de Else y elif

x = 5
if x == 5:
    print("Es 5")
else:
    print("No es 5")

x = 5
if x == 5:
    print("Es 5")
elif x == 6:
    print("Es 6")
elif x ==  7:
    print("Es 7")

x = 5
if x == 5:
    print("Es 5")
elif x == 6:
    print("Es 6")
elif x == 7:
    print("Es 7")
else:
    print("Es otro")


#Operador ternario

x = 5 
print("Es 5" if x == 5 else "No es 5")

a = 10
b = 5
c = a/b if b !=0 else -1

print (c)

x = 6 
if not   x%2:
    print("Es par")
else:
    print("Es inpar")


x = 5
x -= 1 if x>0 else x
print(x)

######Bucles for

for i in range(0,5):
    print(i)

for i in "Python":
    print(i)

#Esto no spermita saber si un elemento es iterable o no 
'''from collections import Iterable

lista = [1, 2, 3, 4]
cadena = "Python"
numero = 10
print(isinstance(lista, Iterable))  #True
print(isinstance(cadena, Iterable)) #True
print(isinstance(numero, Iterable)) #False

#Estoi nos devuelve un iterador del elemento iterable que se le proporcione
lista = [5, 6, 3, 2]
it = iter(lista)
print(it)       #<list_iterator object at 0x106243828>
print(type(it)) #<class 'list_iterator'>'''


#Para manipular un objeto iterable
lista = [5, 6, 3, 2]
it = iter(lista)
print(next(it))
#     [5, 6, 3, 2]
#      ^
#      |
#     it
print(next(it))
#     [5, 6, 3, 2]
#         ^
#         |
#        it
print(next(it))
#     [5, 6, 3, 2]
#            ^
#            |
#           it

#For anidados
lista = [[56, 34, 1],
         [12, 4, 5],
         [9, 4, 3]]

for i in lista:
    print(i)

for i in lista:
    for j in i:
        print(j)

#si se hace uso de [::-1] se puede iterar desde el ultimo elemento

texto = "Python"
for i in texto[::-1]:
    print(i)

texto = "Python"

print("Esto es otro ejercicio")
for i in texto[::-2]:
    print(i)

#usando comprehensions list

print(sum(i for i in range(10)))

#Range

for i in (0, 1, 2, 3, 4, 5):
    print(i) #0, 1, 2, 3, 4, 5

for i in range(6):
    print(i) #0, 1, 2, 3, 4, 5

#range(inicio, fin, salto)

print(list(range(5, 20, 2)))

for i in range(5, 20, 2):
    print(i) #5,7,9,11,13,15,17,19

for i in range (5, 0, -1):
    print(i) #5,4,3,2,1

#Bucles While
x = 5
while x > 0:
    x -=1
    print(x)

#buble whileen una sola linea
x = 5
while x > 0: x-=1; print(x) 

x = ["Uno", "Dos", "Tres"]
while x:
    x.pop(0)
    print(x)

#solo se ejecuta el else cuando el while termina de forma natural 
x = 5
while x > 0:
    x -=1
    print(x) #4,3,2,1,0
else:
    print("El bucle ha finalizado")

x = 5
while True:
    x -= 1
    print(x) #4, 3, 2, 1, 0
    if x == 0:
        break
else:
    # El print no se ejecuta
    print("Fin del bucle")

i = 0
j = 0
while i < 3:
    while j < 3:
        print(i,j)
        j += 1
    i += 1
    j = 0

i, j, k = 0, 0, 0
while i < 3:
    while j < 3:
        while k < 3:
            print(i,j,k)
            k += 1
            j += 1
        k = 0
    i += 1
    j = 0

z = 7
x = 1
while z > 0:
    print(' ' * z + '*' * x + ' ' * z)
    x+=2
    z-=1

text = "Python"
i = 0
while i < len(text):
    print(text[:i + 1])
    i += 1

#####Switch no existe en python lo que se puede hacer es emularlo 

if condicion == 1:
    print("Haz a")
elif condicion == 2:
    print("Haz b")
elif condicion == 3:
    print("Haz c")
else:
    print("Haz d")

#con un elif pero es mas lento podemos generar una tabla y funcionaria como si fuese un switch

if condicion == 1:
    print("1")
elif condicion == 2:
    print("2")

# ... hasta 100
elif condicion == 100:
    print("3")

else:
    print("x")

#emulando un switch
def opera1(operador, a, b):
    if operador == 'suma':
        return a + b
    elif operador == 'resta':
        return a - b
    elif operador == 'multiplica':
        return a * b
    elif operador == 'divide':
        return a / b
    else:
        return None

def opera2(operador, a, b):
    return {
        'suma': lambda: a + b,
        'resta': lambda: a - b,
        'multiplica': lambda: a * b,
        'divide': lambda: a / b
    }.get(operador, lambda: None)

def usa_if(decimal):
    if decimal == '0':
        return "000"
    elif decimal == '1':
        return "001"
    elif decimal == '2':
        return "010"
    elif decimal == '3':
        return "011"
    elif decimal == '4':
        return "100"
    elif decimal == '5':
        return "101"
    elif decimal == '6':
        return "110"
    elif decimal == '7':
        return "111"
    else:
        return "NA"
    
tabla_switch = {
        '0': '000',
        '1': '001',
        '2': '010',
        '3': '011',
        '4': '100',
        '5': '101',
        '6': '110',
        '7': '111',
    }

def usa_switch(decimal):
    return tabla_switch.get(decimal, "NA")

####Iterar con zip en python

a = [1, 2]
b = ["Uno", "Dos"]
c = zip(a, b)

print(list(c))

a = [1, 2]
b = ["Uno", "Dos"]
c = zip(a, b)

for numero, texto in zip(a, b):
    print("Número", numero, "Letra", texto)


numeros = [1, 2]
espanol = ["Uno", "Dos"]
ingles = ["One", "Two"]
frances = ["Un", "Deux"]
c = zip(numeros, espanol, ingles, frances)

for n, e, i, f in zip(numeros, espanol, ingles, frances):
    print(n, e, i, f)

numeros = [1, 2, 3, 4, 5]
espanol = ["Uno", "Dos"]

for n, e in zip(numeros, espanol):
    print(n, e)

numeros = [1, 2, 3, 4, 5]
zz = zip(numeros)
print(list(zz))


numeros = [1, 2, 3, 4, 5]
zz = zip(numeros)
print(list(zz))

a = [1, 2, 3]
b = ["One", "Two", "Three"]
c = zip(a, b)

print(list(c))
# [(1, 'One'), (2, 'Two'), (3, 'Three')]

#asi se pueden obter de un zip en elementos separados 
c = [(1, 'One'), (2, 'Two'), (3, 'Three')]
a, b = zip(*c)

print(a)  # (1, 2, 3)
print(b)  # ('One', 'Two', 'Three')

#Enumerate sirve para obtener los indices cuando se realiza una iteracion
lista = ["A", "B", "C"]

for indice, l in enumerate(lista):
    print(indice, l)

#enumerate esta limitado unicamente a ciclos for 
lista = ["A", "B", "C"]

en = list(enumerate(lista))
print(en)

# Salida;
# [(0, 'A'), (1, 'B'), (2, 'C')]

#List comprehensions

cuadrados = [i**2 for i in range(5)]
#[0, 1, 4, 9, 16]

cuadrados = []
for i in range(5):
    cuadrados.append(i**2)
#[0, 1, 4, 9, 16]

unos = [1 for i in range(5)]
#[1, 1, 1, 1, 1]
=

def eleva_al_2(i):
    return i**2

cuadrados = [eleva_al_2(i) for i in range(5)]
#[0, 1, 4, 9, 16]


lista = [10, 20, 30, 40 , 50]
nueva_lista = [i/10 for i in lista]
#[1.0, 2.0, 3.0, 4.0, 5.0]

#Con condicionales
frase = "El perro de san roque no tiene rabo"
erres = [i for i in frase if i == 'r']
#['r', 'r', 'r', 'r']

print(len(erres))

##Sets comprehension

lista1 = ['nombre', 'edad', 'región']
lista2 = ['Pelayo', 30, 'Asturias']

mi_dict = {i:j for i,j in zip(lista1, lista2)}
#{'nombre': 'Pelayo', 'edad': 30, 'región': 'Asturias'}


#iteradores e iterables  

# Mal uso
lista = [5, 4, 9, 2]
i = 0
while i < len(lista):
    elemento = lista[i]
    print(elemento)
    i += 1
# Salida: 5, 4, 9, 2

# Mal uso
lista = [5, 4, 9, 2]
for i in range(len(lista)):
    elemento = lista[i]
    print(elemento)
# Salida: 5, 4, 9, 2

#una mejor solucion mas limpia y eficiente
lista = [5, 4, 9, 2]
for elemento in lista:
    print(elemento)
# Salida 5, 4, 9, 2

###iterables
cadena = "Hola"
for c in cadena:
    print(c)
# Salida: H o l a

from collections import Iterable

cadena = "Hola"
numero = 3
print("cadena", isinstance(cadena, Iterable))
print("numero", isinstance(numero, Iterable))

# Salida
# cadena True
# numero False

numero = 3
for x in numero:
    print(x)
# Error TypeError: 'int' object is not iterable

print(list("Hola"))
print(sum([1, 2, 3]))
print("-".join("Hola"))

# Salida:
#['H', 'o', 'l', 'a']
#6
#H-o-l-a

mi_dict = {'a':1, 'b':2, 'c':3}
for i in mi_dict:
    print(i)
# Salida: a, b, c

#iteradores

libro = ['página1', 'página2', 'página3', 'página4']
marcapaginas = iter(libro)

print(next(marcapaginas))
print(next(marcapaginas))
print(next(marcapaginas))
print(next(marcapaginas))


# página1
# página2
# página3
# página4

print(next(marcapaginas))
# Salida: StopIteration

###Asi se puede geenrar una clase iterable

class MiClase:
    pass

miobjeto = MiClase()
iterador = iter(miobjeto)

# Salida
# TypeError: 'MiClase' object is not iterable

class MiClase:
    def __init__(self, items):
        self.lista = items
    def __iter__(self):
        return iter(self.lista)


miobjeto = MiClase([5, 4, 3])
for item in miobjeto:
    print(item)

# Salida: 5, 4, 3
