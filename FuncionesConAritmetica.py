import os
os.system('cls' if os.name == 'nt' else 'clear')

#Programa que imprime los resultadosa de las operaciones aritmeticas basicas con funciones

#Declaracion defunciones
def Suma (a,b):
    return (a+b)

def Resta (a,b):
    return (a-b)

def Multiplicacion (a,b):
    return (a*b)

def Division (a,b):
    return (a/b)

def Potencia (a,b):
    return (a**b)

def Raiz (a):
    return a**(1/2)

#Invocaciones de las funciones
print(f"La suma es igual a: {Suma(1, 1)}")
print(f"La resta es igual a: {Resta(1, 1)}")
print(f"La multiplicacion es igual a: {Multiplicacion(2, 2)}")
print(f"La division es igual a: {Division(25, 5)}")
print(f"La potencia es igual a: {Potencia(2, 2)}")
print(f"La raiz cuadrada es igual a: {Raiz(36)}")