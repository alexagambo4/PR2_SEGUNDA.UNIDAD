# PR2_SEGUNDA.UNIDAD
#Este programa pide al usuario que ingrese un número positivo

#El bucle continuará pidiendo números hasta que el usuario ingrese un número negativo


#Inicializamos una variable para almacenar el número ingresado por el usuario

numero = 0

#Comenzamos el bucle while

while numero >= 0:  # Continuar mientras el número sea mayor o igual a cero

    # Pedimos al usuario que ingrese un número
    
    numero = int(input("Ingresa un número positivo (o un número negativo para salir): "))
    
    
    # Verificamos si el número es positivo
    
    if numero >= 0:
    
        print(f"Has ingresado: {numero}")  # Mostramos el número ingresado
        
    else:
    
        print("Has ingresado un número negativo. Saliendo del programa...")  # Mensaje de salida
        

#El programa termina cuando se ingresa un número negativo

![image](https://github.com/user-attachments/assets/b72bb818-a1af-4410-b2e4-2e8ca586dbd2)
