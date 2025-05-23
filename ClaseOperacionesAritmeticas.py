import os
os.system('cls' if os.name == 'nt' else 'clear')

#Clase de operaciones aritméticas 
class OperacionesAritmeticas:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def suma(self):
        return (self.a + self.b)

    def resta(self):
        return (self.a - self.b)

    def multiplicacion(self):
        return (self.a * self.b)

    def division(self):
        if self.b != 0:
            return (self.a / self.b)
        else:
            return "Error: No se puede dividir entre cero"

a = int(input("Ingrese el primer numero: "))
b = int(input("Ingrese el segundo numero: "))

Operacion = OperacionesAritmeticas(a, b)

print("El resultado de la suma es", Operacion.suma())
print("El resultado de la resta es", Operacion.resta())
print("El resultado de la multiplicacion es", Operacion.multiplicacion())
print("El resultado de la division es", Operacion.division())