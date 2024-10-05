# Este programa pide al usuario que ingrese un número positivo.
# El bucle continuará pidiendo números hasta que el usuario ingrese un número negativo.

# Inicializamos una variable para almacenar el número ingresado por el usuario.
numero = 0

# Comenzamos el bucle while
while numero >= 0:  # Continuar mientras el número sea mayor o igual a cero
    # Pedimos al usuario que ingrese un número
    numero = int(input("Ingresa un número positivo (o un número negativo para salir): "))
    
    # Verificamos si el número es positivo
    if numero >= 0:
        print(f"Has ingresado: {numero}")  # Mostramos el número ingresado
    else:
        print("Has ingresado un número negativo. Saliendo del programa...")  # Mensaje de salida

# El programa termina cuando se ingresa un número negativo



#Ejemplos con for 
#Ejemplo no.1
frutas = ["manzana", "plátano", "cereza"]
for fruta in frutas:
    print(fruta)

#Ejemplo no.2
for i in range(5):
    print(i)

#Ejemplo no.3
cuadrados = [x**2 for x in range(10)]
print(cuadrados)
