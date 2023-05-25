import streamlit as st

def pagina_descripcion():
    st.markdown("<h3>Bienvenido a la documentación</h3>", unsafe_allow_html=True)

    # Insertar imagen
    st.image("recursos/dengue-2.jpg", caption="DengueZikaArgentina")

    st.write("""       


Dengue Y Zika en Argentina, se enfoca en filtrar y visualizar por zona y fecha los casos documentados de contagio, para luego ofrecer una prediccion para el año siguiente teniendo en cuenta la curva actual de casos.

A través de análisis exhaustivos, investigación y desarrollo de soluciones, se busca principalmente dar acceso simple y legible a la informacion de casos para un rapido analisis y comprension de la problematica por zonas.

La documentación completa del proyecto está estructurada en secciones lógicas que te guiarán a través de cada aspecto clave. 

Estoy emocionado de compartir contigo la documentación completa del proyecto Dengue y Zika en Argentina! Espero que encuentres la información que buscas y que esta documentación te ayude a comprender mejor el enfoque, metodología y los resultados obtenidos.

Disfruta explorando la documentación y no dudes en contactarme si tienes alguna pregunta o sugerencia: diegomaneyro@gmail.com
""")
# Ruta del archivo PDF que deseas descargar
    ruta_pdf = "../documentacion/documentacion.pdf"

    # Botón de descarga del archivo PDF
    if st.button("Descargar Documentacion"):
        with open(ruta_pdf, "rb") as f:
            bytes_pdf = f.read()
        st.download_button(label="Iniciar descaga", data=bytes_pdf, file_name="Documentacion.pdf", mime="application/pdf")
