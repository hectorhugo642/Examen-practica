alumnos = ["Ana", "Luis", "Paty"]
calif = [9.0, 7.5, 8.2]

# Acceder por indice (desde 0)
print (alumnos[0])    
print (alumnos[-1])   

# Agregar y eliminar
alumnos.append("Carlos")
alumnos.remove("Luis")

# Longitud 
print(len(alumnos))   

# Recorrer
for a in alumnos: 
    print(a)


#=======EJEMPLO PROPIO=======
print ("Ejemplo propio")
jugadores= ["Cristiano Ronaldo", "Messi", "Neymar"]
califXpartido = [8.5, 9, 8]

print (jugadores[0])
print (jugadores[-1])

jugadores.append("Mbappe")
jugadores.remove("Messi")

print(len(jugadores))

for a in jugadores:
    print(a)