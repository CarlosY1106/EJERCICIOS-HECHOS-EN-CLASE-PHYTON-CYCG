import os
os.system('cls' if os.name == 'nt' else 'clear')

#Invocaremos la clase animal
from Clase01 import Perro

MiPerro = Perro ("Rambo")
MiPerro.ladrar()
MiPerro.correr()