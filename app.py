#importar librerias
import pandas as pd
import requests

def descargar_datos_csv(url, archivo_salida):
    """
    Descarga un archivo CSV desde una URL y lo guarda en un archivo local.

    Parámetros:
        - url (str): La URL del archivo CSV a descargar.
        - archivo_salida (str): El nombre del archivo de salida para guardar los datos descargados.
    """
    # Realizar la solicitud GET al enlace y guardar la respuesta
    response = requests.get(url)

    # Verificar si la solicitud fue exitosa (código 200)
    if response.status_code == 200:
        # Guardar los datos en el archivo de salida
        with open(archivo_salida, "wb") as f:
            f.write(response.content)
            print("Descarga completada.")
    else:
        print("Error al descargar los datos. Código de estado:", response.status_code)

url = "http://datos.salud.gob.ar/dataset/ceaa8e87-297e-4348-84b8-5c643e172500/resource/30d76bcb-b8eb-4bf3-863e-c87d41724647/download/informacion-publica-dengue-zika-nacional-anio-2022.csv"
archivo_salida = "datos/datosOriginales/dengue-zika.csv"  # Nombre del archivo de salida en formato CSV

# Descargar los datos desde web
descargar_datos_csv(url, archivo_salida)
