notas = []
total_notas = 0
cantidad_notas = 0
nota_menor = 0
nota_mayor = 0

#Ingreso de notas
while True:
    nota = float(input("Ingrese la nota obtenida (ingrese 0 para finalizar): "))
    if nota != 0:
        notas.append(nota)
        total_notas += nota
        cantidad_notas += 1
        if nota >= 4.0:
            nota_mayor += 1
        else:
            nota_menor += 1
    else:
        break

#Mostrar cantidad de notas
print("\n La cantidad de notas ingresadas es:",len(notas))

#Mostrar promedio de notas
print("El promedio de notas es:", total_notas/cantidad_notas)

#Mostrar cantidad de notas < 4.0
print("La cantidad de notas menores a 4.0 son:", nota_menor)

#Mostrar cantidad de notas > 4.0
print("La cantidad de notas mayores o iguales a 4.0 son:", nota_mayor)