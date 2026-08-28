# python-usos
candidatos_nombres = ["candidato1", "candidato2", "candidato3"]
votos_posibles = ["voto1", "voto2", "voto3"]
contador1 = 0
contador2 = 0
contador3 = 0
while True:
    voto_del_usuario = input("Ingrese el nombre del candidato por el que desea votar (ej. candidato1, candidato2, candidato3): ").lower()
    if voto_del_usuario == candidatos_nombres[0]:
        contador1 += 1
    elif voto_del_usuario == candidatos_nombres[1]:
        contador2 += 1
    elif voto_del_usuario == candidatos_nombres[2]:
        contador3 += 1
    else:
        print("Error: El voto ingresado no corresponde a ningún candidato válido.")
    continuar_votando = input("¿Desea ingresar otro voto? (s/n): ").lower()
    if continuar_votando != 's':
        break 
print(f"Resultados parciales: {candidatos_nombres[0]}: {contador1}, {candidatos_nombres[1]}: {contador2}, {candidatos_nombres[2]}: {contador3}")
if contador1 > contador2 and contador1 > contador3:
    print("Ganador:", candidatos_nombres[0])
elif contador2 > contador1 and contador2 > contador3:
    print("Ganador:", candidatos_nombres[1])
elif contador3 > contador1 and contador3 > contador2:
    print("Ganador:", candidatos_nombres[2])
else:
    if contador1 == contador2 or contador1 == contador3 or contador2 == contador3:
        print("Empate: No hay un ganador único.")
    else:
        print("No se registraron votos suficientes o válidos para determinar un ganador.")
print("Gracias por su voto.")
