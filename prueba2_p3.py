datos_usuarios = {}

#Ingreso de los datos de localidad al usuario
for i in range(5):
    pais = input("Ingrese un pais: ")
    capital = input("Ingrese la capital del pais: ")
    paises[pais] = capital

#Ingreso de nombre del usuario
nombre = input("Ingrese nombre del turista: ")
paisN =input("Ingrese su pais de prosedencia: ")

#Formato
print("El turista con el nombre", nombre ,"viene del pais", paisp,"y su capital es",paises[paisN])
