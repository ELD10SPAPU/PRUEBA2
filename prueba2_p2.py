precios = []

#Ingreso de 10 precios en peso chilenos
for i in range(10):
    precio = int(input("Ingrese el valor de 10 productos en pesos chilenos: "))
    precios.append(precio)

#Convertir los valores de peso chileno a USD
y = 0
for x in precios:
    precios[y] = x/950
    y += 1


print("Los precios de la lista pasados a dolares es:")
print(precios)