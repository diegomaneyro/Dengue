import streamlit as st

def pagina_storytelling():
    st.markdown("### Introduccion al proyecto ")

    #ruta local del video
    video_path = '../recursos/storytelling.mp4'

    #mostrar video
    st.video(video_path)

    st.write("""
    En este resumen del proyecto, se busca como objetivo proporcionar un contexto sólido que enriquezca el análisis realizado y fomente una comprensión más profunda del trabajo llevado a cabo.""")