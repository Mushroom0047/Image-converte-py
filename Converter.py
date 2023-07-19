from tkinter import Tk
from tkinter.filedialog import askopenfilenames
from PIL import Image
import os

def convertir_a_webp():
    # Crea una instancia de Tkinter y ocúltala
    root = Tk()
    root.withdraw()

    # Muestra el cuadro de diálogo para seleccionar múltiples archivos de imagen
    archivos = askopenfilenames(filetypes=[("Archivos de imagen", "*.png;*.jpg;*.jpeg")], multiple=True)

    # Verifica si el usuario seleccionó archivos
    if archivos:
        # Crea una carpeta para almacenar los archivos convertidos
        carpeta_destino = "archivos_webp"
        if not os.path.exists(carpeta_destino):
            os.makedirs(carpeta_destino)
        
        # Itera sobre los archivos seleccionados
        for archivo in archivos:
            # Abre el archivo de imagen
            imagen = Image.open(archivo)

            # Crea el nombre del archivo WebP utilizando el mismo nombre de archivo pero con la extensión cambiada a .webp
            nombre_archivo_webp = os.path.splitext(os.path.basename(archivo))[0] + ".webp"

            # Guarda la imagen en formato WebP en la carpeta destino
            ruta_destino = os.path.join(carpeta_destino, nombre_archivo_webp)
            imagen.save(ruta_destino, "WebP")

        print("Archivos convertidos y guardados en la carpeta:", carpeta_destino)

        # Abre la carpeta destino
        os.system(f'explorer "{carpeta_destino}"')

convertir_a_webp()
