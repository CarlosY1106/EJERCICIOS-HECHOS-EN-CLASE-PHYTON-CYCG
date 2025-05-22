#Codigo para limpiar la consola
import os
os.system('cls' if os.name == 'nt' else 'clear')

#Crear un programa que calcule el total a pagar por un solo producto, incluyendo ISV. 
#Si el subtotal supera los 10,000, aplicar un 25% de descuento antes de calcular el impuesto. Mostrar el total final.

TotalCompra= 0
Descuento=0.25
Isv=0.15

ValorCompra= float(input("Por favor ingrese el valor de la compra por un producto: "))
if ValorCompra >= 10000:
    Descuento=0.25
else:
    Descuento=0
TotalCompra= ValorCompra - (ValorCompra * Descuento)
TotalCompra= TotalCompra + (TotalCompra * Isv)
print(f"El total de la compra por un producto es igual a: {TotalCompra}")
