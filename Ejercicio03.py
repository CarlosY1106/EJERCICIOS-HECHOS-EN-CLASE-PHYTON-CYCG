import os
os.system('cls' if os.name == 'nt' else 'clear')

#Hacer un programa que imprima la tabla de multiplicar del numero que el usuario ingrese.
TablaMultiplicar = int(input("Por favor ingrese el numero de la tabla de multiplicar que quiere ver: "))
print("TABLA DE MULTIPLICAR DEL", TablaMultiplicar)
for i in range (1,11):
    print (TablaMultiplicar, "x", i, "=", TablaMultiplicar*i)