def mostrar_menu():
    print("Bienvenido al generador de códigos QR")
    
    # Capturar el tamaño del código QR
    while True:
        try:
            tamano = int(input("Ingrese el tamaño de la matriz (por ejemplo, 21 para un código QR básico): "))
            if tamano < 21 or tamano > 177:
                print("El tamaño debe ser entre 21 y 177.")
            else:
                break
        except ValueError:
            print("Por favor, ingrese un número válido.")
    
    # Capturar el texto que se codificará en el QR
    texto = input("Ingrese el texto o URL que desea codificar en el QR: ")

    return tamano, texto
