from PIL import Image
import os

# Ruta de la carpeta con las imágenes
carpeta_imagenes = "rutaa"

# Ruta de la carpeta donde se guardarán las imágenes convertidas
carpeta_salida = "rutab"

# Lista de extensiones de archivo de imagen válidas
extensiones_validas = [".jpg", ".jpeg", ".png"]

# Recorremos todas las imágenes de la carpeta
for archivo in os.listdir(carpeta_imagenes):
    # Comprobamos que el archivo es una imagen válida
    if archivo.endswith(tuple(extensiones_validas)):
        # Abrimos la imagen con Pillow
        ruta_archivo = os.path.join(carpeta_imagenes, archivo)
        imagen = Image.open(ruta_archivo)
        
        # Creamos la ruta de salida
        ruta_salida = os.path.join(carpeta_salida, os.path.splitext(archivo)[0] + ".webp")
        
        # Convertimos la imagen y la guardamos en formato WebP
        imagen.save(ruta_salida, "webp")