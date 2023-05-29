import os
import pandas as pd
import requests

def descargar_datos_csv(url, nombre_archivo):
    """
    Descarga un archivo CSV desde una URL y lo guarda en la ubicación especificada.

    Parámetros:
        - url (str): La URL del archivo CSV a descargar.
        - nombre_archivo (str): El nombre del archivo para guardar los datos descargados.
    """
    response = requests.get(url)
    if response.status_code == 200:
        ruta_guardado = os.path.join(os.getcwd(), nombre_archivo)
        with open(ruta_guardado, "wb") as f:
            f.write(response.content)
        print("Descarga completada. Archivo guardado en:", ruta_guardado)
    else:
        print("Error al descargar los datos. Código de estado:", response.status_code)

# Ejemplo de uso
url = "http://datos.salud.gob.ar/dataset/ceaa8e87-297e-4348-84b8-5c643e172500/resource/30d76bcb-b8eb-4bf3-863e-c87d41724647/download/informacion-publica-dengue-zika-nacional-anio-2022.csv"
nombre_archivo = "datos/datosOriginales/dengue-zika.csv"

# Descargar los datos en la carpeta actual o adyacente
descargar_datos_csv(url, nombre_archivo)
