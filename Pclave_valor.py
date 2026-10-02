alumno = {
"nombre": "Ana López"
"grupo": "ЗА"
"calificaciones": [8.5, 9.0, 7.5]
}

# Acceder
print (alumno ["nombre"]) # "Ana lopez"

# Agregar / modificar
alumno["email"] = "ana@mail.com"
alumno["grupo"] = "3B"

# Recorrer
# clAVE Y VALOR
for clave, valor in alumno.items ():
    print (f"{clave}: {valor}")

# Valores
for valor in alumno.values():
    print (valor)

# Claves
for clave in alumno: