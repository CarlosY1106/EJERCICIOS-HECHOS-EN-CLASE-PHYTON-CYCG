#Codigo para limpiar la consola
import os
os.system('cls' if os.name == 'nt' else 'clear')

#Hacer un programa para calcular la edad a partir del año de nacimiento de una persona.
AnioActual = 2025
Edad = 0
AnioNacimiento = float (input("Por favor ingrese su año de nacimiento: "))
Edad = (AnioActual - AnioNacimiento)

print ("Su edad actualmente es: ", Edad)

if Edad >= 21:
    print("Usted es mayor de edad")
else:
    print("Usted es menor de edad en el rango de los 21 años")
    
if Edad >= 18:
    print("Usted es ciudadano, ya puede ejercer su derecho al voto")
else:
    print("Usted es menor de edad, no puede ejercer su derecho al voto")
