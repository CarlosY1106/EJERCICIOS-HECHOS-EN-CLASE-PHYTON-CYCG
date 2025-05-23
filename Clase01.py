import os
os.system('cls' if os.name == 'nt' else 'clear')

#Creando la clase animal
#Clases con el primer nombre en mayuscula

class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def comer(self):
        print(f"{self.nombre} el animal esta comiendo")

    def correr(self):
        print(f"{self.nombre} esta corriendo")

class Perro(Animal):
    def ladrar(self):
        print(f"{self.nombre} gua gua gua")

# Definir objetos para usar las clases
perro = Perro("Rufus")
perro.correr()
perro.ladrar()
perro.comer()

gato = Animal("Misio")
gato.correr()
gato.comer()