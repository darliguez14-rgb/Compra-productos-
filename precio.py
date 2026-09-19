def calcular_total(precio, cantidad):
    total = precio * cantidad
    return total
precio = float(input("Ingrese el precio del producto: $"))
cantidad = int(input("Ingrese la cantidad de productos: "))
total_compra = calcular_total(precio, cantidad)
print("El precio total de la compra es: $", total_compra)