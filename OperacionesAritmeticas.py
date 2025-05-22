#Codigo para limpiar la consola
import os
os.system('cls' if os.name == 'nt' else 'clear')

#Programa que hace operaciones aritméticas básicas
a = 10
b = 5

#Suma
Suma = (a + b)
print(f"{a} + {b} = {Suma}")

#Resta
Resta = (a - b)
print(f"{a} - {b} = {Resta}")

#Multiplicacion
Multi = (a * b)
print(f"{a} * {b} = {Multi}")

#División
Div = (a / b)
print(f"{a} / {b} = {Div}")

#Ingreso de valores a variables
X = int(input("x: "))
y = int(input("y: "))

#Potencia
Potencia = X ** y
print(f"{X} ^ {y} = {Potencia}")

#Operador de residuo
Residuo = X % y
print(f"{X} % {y} = {Residuo}")

#Raiz cuadrada
Raiz = X ** (1/2)
print(f"Raiz cuadrada de {X} = {Raiz}")