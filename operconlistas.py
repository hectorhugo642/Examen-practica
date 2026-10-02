calif = [8.5, 7.0, 9.2, 6.5, 8.0]

# Funciones 
print(max(calif))
print(min(calif))
print(sum(calif))
prom = sum(calif) / len(calif)

# Ordenar
# ascendente
calif.sort()
# descendente
calif.sort(reverse=True)

# Slicing los primeros que quieras
top3 = calif[:3]

# List comprehension (filtrado datos)
aprobados = [c for c in calif if c >= 6]



#==================EjemploMilo===========
calif = [9.0, 9.6, 7.0, 6.7, 8.0]

# Funciones 
print(max(calif))
print(min(calif))
print(sum(calif))
prom = sum(calif) / len(calif)

# Ordenar
# ascendente
calif.sort()
# descendente
calif.sort(reverse=True)

# Slicing los primeros que quieras
top3 = calif[:3]

# List comprehension (filtrado datos)
aprobados = [c for c in calif if c >= 7]
