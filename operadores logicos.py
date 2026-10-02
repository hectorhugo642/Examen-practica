print("----ejemplo---")

edad=18
tiene_identificacion= True
es_estudiante= False

if edad>=18 and tiene_identificacion:
    print("Cumples ambas condiciones")

if edad>=18 or es_estudiante:
    print("Cumples al menos una condicion")

if not es_estudiante:
    print("No es estudiante")

print("----propio------")

creditos=260
tesis=True
servicio_social=False

if creditos>=260 and tesis:
    print("graduado")

if creditos>=260 or servicio_social:
    print("llevas un requisito por lo menos")

if not servicio_social:
    print("no tienes servicio social")


