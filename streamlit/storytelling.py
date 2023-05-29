import streamlit as st

def pagina_storytelling():
    st.markdown("### Introduccion al proyecto ")

    #ruta local del video
    video_path = 'https://drive.google.com/file/d/1_l-2gXw7g32gR2OnOsz19JuxKpOGRH5u/view?usp=drive_link'

    #mostrar video
    st.video(video_path)

    st.write("""
    En este resumen del proyecto, se busca como objetivo proporcionar un contexto sólido que enriquezca el análisis realizado y fomente una comprensión más profunda del trabajo llevado a cabo.""")
