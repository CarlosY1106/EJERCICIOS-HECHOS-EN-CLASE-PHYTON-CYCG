#Codigo para limpiar la consola
import os
os.system('cls' if os.name == 'nt' else 'clear')

#Crear un programa utilizando una funcion que calcule el total a pagar por un solo producto, incluyendo ISV. 
#Si el subtotal supera los 10,000, aplicar un 25% de descuento antes de calcular el impuesto. Mostrar el total final.

def CalcularTotal(ValorCompra, Descuento, Isv):
    if ValorCompra >= 10000:
        DescuentoAplicado = Descuento
    else:
        DescuentoAplicado = 0
    Subtotal = ValorCompra - (ValorCompra * DescuentoAplicado)
    Total = Subtotal + (Subtotal * Isv)
    return Total

ValorCompra = float(input("Por favor ingrese el valor de la compra por un producto: "))
Descuento = 0.25
Isv = 0.15

TotalCompra = CalcularTotal(ValorCompra, Descuento, Isv)
print(f"El total de la compra por un producto es igual a: {TotalCompra}")