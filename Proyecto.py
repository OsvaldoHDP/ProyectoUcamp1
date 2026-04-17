# Solicitamos el nombre y apellidos del usuario
# El bucle while se repite hasta que el usuario introduzca un valor no vacío
nombre = ""
while nombre == "":
    nombre = input("Ingresa tu nombre: ").strip()#.strip para validar que entre al if si no se ingresa nada
    if nombre == "":
        print("Error: el nombre no puede estar vacío. Intenta de nuevo.")

apellidoPaterno = ""
while apellidoPaterno == "":
    apellidoPaterno = input("Ingresa tu apellido paterno: ").strip()
    if apellidoPaterno == "":
        print("Error: el apellido paterno no puede estar vacío. Intenta de nuevo.")

apellidoMaterno = ""
while apellidoMaterno == "":
    apellidoMaterno = input("Ingresa tu apellido materno: ").strip()
    if apellidoMaterno == "":
        print("Error: el apellido materno no puede estar vacío. Intenta de nuevo.")

# --- CAPTURA Y VALIDACIÓN DE DATOS NUMÉRICOS ---
# Validación de edad (int)
edadValida = False
while edadValida == False:
    edadIngresada = input("Ingresa tu edad (años): ").strip()
    if edadIngresada == "":
        print("Error: la edad no puede estar vacía. Intenta de nuevo.")
    else:
        try:
            edad = int(edadIngresada)
            if edad <= 0:
                print("Error: la edad debe ser un número positivo. Intenta de nuevo.")
            else:
                edadValida = True
        except ValueError:
            print("Error: debes ingresar un número entero para la edad. Intenta de nuevo.")

# Validación de peso en kilogramos (número decimal)
pesoValido = False
while pesoValido == False:
    pesoIngresado = input("Ingresa tu peso en kg (ejemplo: 70.5): ").strip()
    if pesoIngresado == "":
        print("Error: el peso no puede estar vacío. Intenta de nuevo.")
    else:
        try:
            peso = float(pesoIngresado)
            if peso <= 0:
                print("Error: el peso debe ser un número positivo. Intenta de nuevo.")
            else:
                pesoValido = True
        except ValueError:
            print("Error: debes ingresar un número para el peso. Intenta de nuevo.")

# Validación de estatura en metros (número decimal)
estaturaValida = False
while estaturaValida == False:
    estaturaIngresada = input("Ingresa tu estatura en metros (ejemplo: 1.70): ").strip()
    if estaturaIngresada == "":
        print("Error: la estatura no puede estar vacía. Intenta de nuevo.")
    else:
        try:
            estatura = float(estaturaIngresada)
            if estatura <= 0:
                print("Error: la estatura debe ser un número positivo. Intenta de nuevo.")
            else:
                estaturaValida = True
        except ValueError:
            print("Error: debes ingresar un número para la estatura. Intenta de nuevo.")

# --- CÁLCULO DEL IMC ---
# Fórmula: IMC = peso / (estatura al cuadrado)
imc = peso / (estatura ** 2)

# Redondeamos el resultado a 2 decimales para mejor lectura
imcRedondeado = round(imc, 2)

# --- CLASIFICACIÓN DEL IMC ---
if imcRedondeado < 18.5:
    clasificacion = "Bajo peso"
elif imcRedondeado < 25.0:
    clasificacion = "Peso normal"
elif imcRedondeado < 30.0:
    clasificacion = "Sobrepeso"
else:
    clasificacion = "Obesidad"

# Imprimimos todos los datos del usuario junto con su IMC calculado
print("\n--- Aqui estan tus datos ---")
print("Nombre: " + nombre + " " + apellidoPaterno + " " + apellidoMaterno)
print("Edad: " + str(edad) + " años")
print("Peso: " + str(peso) + " kg")
print("Estatura: " + str(estatura) + " m")
print("\nTu IMC es: " + str(imcRedondeado))
print("Eso significa que tienes: " + clasificacion)