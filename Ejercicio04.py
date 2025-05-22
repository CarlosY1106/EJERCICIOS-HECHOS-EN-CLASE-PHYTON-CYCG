import os
os.system('cls' if os.name == 'nt' else 'clear')

#Programa que imprime la tabla de multiplicar del numero que ingrese el usuario usando el ciclo while

i = 1
Num = int(input("Por favor ingrese el numero de la tabla de multiplicar que desea ver: "))
print("La tabla de multiplicar del ", Num, " es: ")
while i <= 10:
    print(Num, "x", i, "=", Num * i)
    i += 1