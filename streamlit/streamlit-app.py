"""
Streamlit de documentacion para el projecto de Dengue 
en Argentinma desde el año 2022 
"""
import streamlit as st
import descripcion
import documentacion
import analisis

def main():
    #Panel lateral
    st.sidebar.title("Menu")

    page = st.sidebar.radio("Selecciona una página", ("Introducción","Análisis de Datos","Documentación"))
    
    # Muestra la página correspondiente según la selección
    if page == "Introducción":
        descripcion.pagina_descripcion()
    elif page == "Documentación":
        documentacion.pagina_documentacion()
    else:
        analisis.pagina_analisis()

    

if __name__ == "__main__":
    main()
