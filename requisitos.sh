#!/bin/bash

# Actualizar los repositorios de paquetes
echo "Actualizando los repositorios..."
sudo apt update

# Instalar pip si no está instalado
if ! command -v pip &> /dev/null
then
    echo "Pip no está instalado. Instalando pip..."
    sudo apt install -y python3-pip
else
    echo "Pip ya está instalado."
fi

# Instalar tkinter si no está instalado
echo "Instalando tkinter (para la interfaz gráfica)..."
sudo apt install -y python3-tk

# Instalar Pillow (biblioteca para trabajar con imágenes)
echo "Instalando Pillow..."
pip install --upgrade pillow

# Finalización
echo "Instalación completa. Todas las dependencias deberían estar instaladas correctamente."
