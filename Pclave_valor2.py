# Diccionario de productos
producto = {
    "nombre": "Laptop",
    "marca": "Lenovo",
    "precio": 12500,
    "stock": 8
}

# Acceder a un valor
print(producto["nombre"])

# Agregar un elemento
producto["categoria"] = "Computación"

# Modificar un elemento
producto["precio"] = 12000

# Recorrer clave y valor
for clave, valor in producto.items():
    print(f"{clave}: {valor}")

# Mostrar solo los valores
for valor in producto.values():
    print(valor)

# Mostrar solo las claves
for clave in producto:
    print(clave)