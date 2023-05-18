# Vamos a observar como funcionan las estructuras de control

saludo = True

if saludo:
    print("Hola mundo")
else:
    print("No hay saludos")

is_online = True

if is_online:
    print("Daniel is online")

respuesta = "Lagarto"

if respuesta == "Lagarto":
    print(respuesta, "es correcto")

edad = 18
if edad >= 18:
    print("Es mayordeedad")

nota = 80

if nota < 60:
    print("El alumno se quedó")
elif nota < 70:
    print("EL alumno va a convocatoria")
else:
    print("El alumno pasó el año")



# Vamos a realizar ejemplos de bucles o ciclos 

# Variables de control

num1 = 1


# Bucle mientras o While

control = True

while control == True:
    print(num1)
    num1 += 1
    if num1 == 101:
        control = False



contador = 0
online = True
num2 = 1
while contador < 100 and online:
    print(num2)
    num2 +=1
    contador += 1

# Bucle o ciclo For

for i in range(4):
    print(i)

for c in range(2):
    print("we will")
print("rock you")