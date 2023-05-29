import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def pagina_analisis():
    st.markdown("<h3>Análisis de casos Dengue y Zika 2022</h3>", unsafe_allow_html=True)

    st.write(
    """
    Análisis de la problematica de Dengue y Zika en Argentina
    """)
    
    #cargar datos desde csv
    ruta_datos ="../datos/limpieza/eda/dengue-zika-clean.csv" 
    
    df = pd.read_csv(ruta_datos)  

    #mostrar primeras filas del dataframe
    if st.button('Mostrar primeras filas del DataFrame'):
        st.dataframe(df.head())
    
    #mostrar grafica de casos por provincia
    if st.button('Mostrar casos por provincia'):
        casos_por_provincia = df.groupby('provincia')['cantidad_casos'].sum()
        fig, ax = plt.subplots()
        casos_por_provincia.plot(kind='bar', ax=ax)
        ax.set_xlabel='Provincia'
        ax.set_ylabel='Casos'
        ax.set_title='Casos por Provincia'
        st.pyplot(fig)

    if st.button('Mostrar casos por edad'):
        casos_por_franja_etaria = df.groupby('grupo_etario')['cantidad_casos'].sum()
        fig, ax = plt.subplots()
        casos_por_franja_etaria.plot(kind='bar', ax=ax)
        ax.set_xlabel='Franja etaria'
        ax.set_ylabel='Casos'
        ax.set_title='Casos por Franja etaria'
        st.pyplot(fig)
    
