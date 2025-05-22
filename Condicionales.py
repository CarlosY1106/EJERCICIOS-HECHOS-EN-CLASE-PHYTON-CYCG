#Codigo para limpiar la consola
import os
os.system('cls' if os.name == 'nt' else 'clear')

#Condicionales en python
a = 0

if a %2==0:
    print (f"{a} es par.")
else:
    print (f"{a} es impar.") 
if a == 0:
    print (f"{a} no es par ni impar.")