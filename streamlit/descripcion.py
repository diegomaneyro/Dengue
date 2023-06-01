import streamlit as st
from PIL import Image

def pagina_descripcion():
    st.markdown("<h3>Dengue en Argentina 2022</h3>", unsafe_allow_html=True)
    # Colocar una línea separadora personalizada
    st.markdown("---")
    
    # Insertar imagen
        
    st.image("recursos/dengue-2.jpg")
    
    st.write("""     
Este proyecto se enfoca en realizar un análisis de los datos, filtrando por zona y fecha los casos documentados de contagio, para luego ofrecer una prediccion para el año siguiente teniendo en cuenta la curva actual de casos.

A través de análisis exhaustivos, investigación y desarrollo de soluciones, se busca principalmente dar acceso simple y legible a la informacion de casos para un rapido analisis y comprension de la problematica por zonas.

La documentación completa del proyecto está estructurada en secciones lógicas que te guiarán a través de cada aspecto clave. 

Estoy emocionado de compartir contigo la documentación completa del proyecto !Dengue en Argentina 2022!. Espero que encuentres la información que buscas y que esta documentación te ayude a comprender mejor el enfoque, metodología y los resultados obtenidos.

""")
    # Colocar una línea separadora personalizada
    st.markdown("---")
    st.write("""
Disfruta explorando la documentación y no dudes en contactarme si tienes alguna pregunta o sugerencia: diegomaneyro@gmail.com
   
   """)
