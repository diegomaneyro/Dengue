import streamlit as st

def pagina_documentacion():
    
    st.markdown("<h3>Documentación</h3>", unsafe_allow_html=True)

    st.write("""
Documentación del Proyecto: Análisis de casos de Dengue y Zika en Argentina
Descripción del Proyecto

El proyecto "Análisis de casos de Dengue y Zika en Argentina" tiene como objetivo recopilar, analiza
de dengue y zika registrados en Argentina. Utilizando fuentes de datos confiables proporcionadas po
brindar información actualizada y detallada sobre la incidencia de estas enfermedades transmitidas 

Objetivos

Recopilar y procesar los datos oficiales de los casos de dengue y zika en Argentina.

Realizar un análisis epidemiológico de la evolución temporal de los casos.
Identificar las regiones y provincias más afectadas por el dengue y zika.
Visualizar los datos de manera clara y accesible mediante gráficos y mapas interactivos.
Proporcionar información útil para los profesionales de la salud y el público en general sobre la preve
Tecnologías Utilizadas

El proyecto se desarrollará utilizando las siguientes tecnologías:

Lenguaje de programación: Python 3
Bibliotecas y frameworks: Pandas, Matplotlib, Seaborn, Folium
Base de datos: MySQL
Herramienta de visualización: Visual Studio Code, Jupyter Notebook

Proceso de Trabajo
Recopilación de datos:
Descarga de los datos oficiales del sitio web del Ministerio de Salud de Argentina.
Limpieza y preparación de los datos para su análisis.
Análisis de datos:

Exploración de los datos para identificar patrones y tendencias.
Cálculo de estadísticas descriptivas, como tasas de incidencia y distribución geográfica.
Análisis de la evolución temporal de los casos.
Visualización de datos:

Creación de gráficos y visualizaciones interactivas para representar los datos de manera clara y com
Generación de mapas temáticos que muestren la distribución geográfica de los casos.
Documentación y presentación:

Documentación detallada de los pasos realizados, metodologías y resultados obtenidos.
Preparación de informes y presentaciones visuales para compartir los hallazgos del proyecto.
Resultados Esperados

Al finalizar el proyecto, se espera obtener:
Un análisis completo de los casos de dengue y zika en Argentina, con una descripción detallada de l
Gráficos y visualizaciones interactivas que permitan explorar y comprender los datos de manera intui
Mapas temáticos que muestren la distribución geográfica de los casos en diferentes regiones y provi
Información útil y actualizada sobre la incidencia de estas enfermedades para los profesionales de la

Consideraciones Éticas y de Privacidad
Durante el desarrollo del proyecto, se garantizará el cumplimiento de las regulaciones éticas y de priv
fuentes de datos oficiales y se respetará la confidencialidad de la información personal de los pacien
y se seguirán todas las normativas y mejores prácticas en la gestión de datos sensibles.
    """)
