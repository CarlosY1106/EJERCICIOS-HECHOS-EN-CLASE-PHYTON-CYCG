import os
os.system('cls' if os.name == 'nt' else 'clear')

def saludo(nombre):
    print(f"Hola {nombre}")

def _Pi():
    return 3.1416

def suma(a, b):
    return a + b

saludo("Carlitos Chávez")

#Calcular el diametro de un circulo
R = 10
Diametro = 2 * _Pi() * R
print (f"El diametro del circulo es: {Diametro}")

#Funcion suma
print(f"La suma es igual a: {suma(1, 1)}")