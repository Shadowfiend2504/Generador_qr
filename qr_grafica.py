from PIL import Image, ImageTk
import tkinter as tk
import os

def mostrar_qr(matriz_qr, tamano_matriz):
    # Crear una imagen vacía (en blanco)
    tamano_celda = 10  # Tamaño de cada celda del QR
    tamano_imagen = tamano_matriz * tamano_celda
    imagen = Image.new("RGB", (tamano_imagen, tamano_imagen), "white")
    pixels = imagen.load()

    # Rellenar la imagen basándonos en la matriz QR
    for i in range(tamano_matriz):
        for j in range(tamano_matriz):
            color = (0, 0, 0) if matriz_qr[i][j] == 1 else (255, 255, 255)
            for x in range(tamano_celda):
                for y in range(tamano_celda):
                    pixels[i * tamano_celda + x, j * tamano_celda + y] = color

    # Guardar la imagen como JPG
    guardar_qr(imagen)

    # Mostrar la imagen con tkinter
    mostrar_qr_interfaz(imagen)

def guardar_qr(imagen):
    # Guardar en el escritorio del usuario
    ruta_escritorio = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    ruta_archivo = os.path.join(ruta_escritorio, 'codigo_qr.jpg')
    imagen.save(ruta_archivo, "JPEG")
    print(f"QR guardado en: {ruta_archivo}")

def mostrar_qr_interfaz(imagen):
    # Crear una ventana de tkinter
    root = tk.Tk()
    root.title("Código QR")

    # Convertir la imagen de PIL a un formato compatible con tkinter
    img_tk = ImageTk.PhotoImage(imagen)

    # Crear un label y mostrar la imagen
    label = tk.Label(root, image=img_tk)
    label.image = img_tk  # Para evitar que sea recolectada por el garbage collector
    label.pack()

    # Botón para cerrar la ventana
    btn_cerrar = tk.Button(root, text="Cerrar", command=root.destroy)
    btn_cerrar.pack()

    # Ejecutar la ventana de tkinter
    root.mainloop()
