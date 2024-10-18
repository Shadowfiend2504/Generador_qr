from menu import mostrar_menu
from qr_generador import generar_qr
from qr_grafica import mostrar_qr

def main():
    # Llamamos al menú inicial para definir el tamaño del QR y capturar la información a codificar
    tamano_matriz, texto = mostrar_menu()

    # Generamos la matriz QR basada en el texto
    matriz_qr = generar_qr(tamano_matriz, texto)

    # Mostramos y guardamos el código QR
    mostrar_qr(matriz_qr, tamano_matriz)

if __name__ == "__main__":
    main()
