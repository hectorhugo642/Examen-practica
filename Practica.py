#Declaramos lo que ocupamos arreglo(calificaciones) y variable(nombre)
calificaciones=[]
nombre=input(f"Dame el nombre del reprobado (xd es broma): ")

#Pedimos las calificaciones
for i in range (3):
    calificacion = float(input(f"Ingrese del 1 al 100 la calificación {i+1}: "))
    calificaciones.append(calificacion)

#Saca el promedio y empiesa a imprimir
promedio = (calificaciones[0]+calificaciones[1]+calificaciones[2])/3
print(f"El alumno {nombre} tiene las calificaciones: ")

#Imprimir las calificaciones y el promedio se imprime maximo 2 decimales
for i in range (3):
    print(f"Calificacion{i+1}")
    print(calificaciones[i])
print(f"Con promedio de :{promedio:.2f}")

#Vemos si esta Reprobados o Aprobados
if(promedio <= 60):
    print("Y si esta reprobado no mentia :(")
else:
    print("Y el alumno esta aprobado :D")
    