import streamlit as st

def pagina_storytelling():    
    st.markdown("<h3>Dengue en Argentina 2022</h3>", unsafe_allow_html=True)
    # Colocar una línea separadora personalizada
    st.markdown("---")
    #ruta local del video


    video_path = '../recursos/storytelling.mp4'
   video_path = 'https://drive.google.com/file/d/1_l-2gXw7g32gR2OnOsz19JuxKpOGRH5u/view?usp=drive_link'


    #mostrar video
    st.video(video_path)

    st.write("""
    En este resumen del proyecto, se busca como objetivo proporcionar un contexto sólido que enriquezca el análisis realizado y fomente una comprensión más profunda del trabajo llevado a cabo.""")
