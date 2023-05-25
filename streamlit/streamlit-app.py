"""
Streamlit de documentacion para el projecto de Dengue y Zika
en Argentinma desde el año 2022 
"""
import streamlit as st
import descripcion
import documentacion


def main():
    #Panel lateral
    st.sidebar.title("Dengue y Zika en Argentina")

    page = st.sidebar.radio("Selecciona una página", ("Descripción del Proyecto", "Documentación Completa"))
    
    # Muestra la página correspondiente según la selección
    if page == "Descripción del Proyecto":
        descripcion.pagina_descripcion()
    elif page == "Documentación Completa":
        documentacion.pagina_documentacion()

    

if __name__ == "__main__":
    main()
