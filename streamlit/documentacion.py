import streamlit as st

def pagina_documentacion():
    st.markdown("<h3>Dengue en Argentina 2022</h3>", unsafe_allow_html=True)
    # Colocar una línea separadora personalizada
    st.markdown("---")
    
    st.write("""

El proyecto "Dengue en Argentina" tiene como objetivo recopilar, analizar los casos de dengue registrados en Argentina.
Utilizando fuentes de datos confiables proporcionadas por
el Gobierno de la Nacion Argentina desde la web Oficial www.datos.gob.ar. Este proyecto busca brindar información actualizada y detallada. 
""")
    st.markdown("#### Objetivos")
    st.write("""
Recopilar y procesar los datos oficiales de los casos de dengue en Argentina.
Realizar un análisis epidemiológico de la evolución temporal de los casos.
Identificar las regiones y provincias más afectadas por el dengue.
Visualizar los datos de manera clara y accesible mediante gráficos y mapas interactivos.
Proporcionar información útil para los profesionales de la salud y el público en general.
""")
    st.markdown("#### Herramientas Utilizadas")
    st.write("""

* Lenguaje de programación: Python
* Bibliotecas: Pandas, Matplotlib, Seaborn 
* Frameworks: Streamlit: www.share.streamlit.io
* Herramienta de visualización: Visual Studio Code, Jupyter Notebook
* Repositorio: Github: www.github.com
* Control de versiones: Git


""")
    st.markdown("#### Proceso de trabajo")
    st.write("""


* Recopilación de datos:
Mediante Pipelines de automatización se realiza la descarga de los datos oficiales del sitio web del Ministerio de Salud de Argentina.
Limpieza y preparación de los datos para su análisis.

* Análisis de datos:
Exploración de los datos para identificar patrones y tendencias.
Cálculo de estadísticas descriptivas, como tasas de incidencia y distribución geográfica.
Análisis de la evolución temporal de los casos.

* Visualización de datos:
Creación de gráficos y visualizaciones interactivas para representar los datos de manera clara.

* Documentación y presentación:
Documentación detallada de los pasos realizados, metodologías y resultados obtenidos.
Preparación de informes y presentaciones visuales para compartir los hallazgos del proyecto.
Resultados Esperados.

""")
    st.markdown("#### Al finalizar el proyecto, se espera obtener")
    st.write("""

Un análisis completo de los casos de dengue en Argentina en 2022, con una descripción detallada.
Gráficos y visualizaciones interactivas que permitan explorar y comprender los datos de manera intuitiva de los casos en diferentes regiones y provincias,
información útil y actualizada sobre la incidencia de estas enfermedades para los profesionales de la salud y publico en gral.

Consideraciones Éticas y de Privacidad
Durante el desarrollo del proyecto, se garantizará el cumplimiento de las regulaciones éticas y de privacidad.
las fuentes de datos son oficiales y se respetará las regulaciones sobre el manejo de informacion publica. 
Se seguirán todas las normativas y mejores prácticas en la gestión de datos sensibles.
""")
# Colocar una línea separadora personalizada
    st.markdown("---")
    
    #Crear columnas
    col1, col2 = st.columns(2)
    
    with col1:        
        
        st.markdown("#### Repositorio")
        st.write("""
        Aquí encontraraa el link al repositorio de este proyecto
        """)
        
        # URL del repositorio
        repo_url = "https://github.com/diegomaneyro/DengueZikaArgentina"
    
        # Mostrar el enlace al repositorio
        st.markdown(f"[Enlace al repositorio]({repo_url})")
               
        
    with col2:        
        
        st.markdown("#### Licencia")
        
        st.write("""
        Este proyecto se distribuye bajo la Licencia MIT. Puedes encontrar los términos y condiciones de la licencia en este enlace 
        Licenica MIT
        """)

        Licenica_url = "https://opensource.org/license/mit/"
        
        #Licencia
        st.markdown(f'[Enlace a la licencia]({Licenica_url})')
