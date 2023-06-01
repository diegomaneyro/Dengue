import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def pagina_analisis():
    st.markdown("<h3>Dengue en Argentina 2022</h3>", unsafe_allow_html=True)
    # Colocar una línea separadora personalizada
    st.markdown("---")

    st.markdown(' Casos de Dengue en Argentina 2022')

    #cargar datos desde csv

    ruta_datos = "../datos/limpieza/eda/dengue-zika-clean.csv"
    df = pd.read_csv(ruta_datos)
    
    #mostrar primeras filas del dataframe
    if st.button('Mostrar Datos'):
        st.dataframe(df.head())

    
    # Colocar una línea separadora personalizada
    st.markdown("---")

    with st.expander("Opciones de gráficas"):
        st.markdown("""
                Seleccione la columna que desea visualizar, luego elija la gráfica:
                
                * Columnas: Provincia, Localidad, Grupo Etario, Semanas Epidemiologicas
                
                * Gráficas: Lineplot, Barchat, Barras, Dispersión 

                Semanas Epidemiologicas solo se admite en gráfico de Dispersión.
                """)
       
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

    

    # Crear el selector
    st.sidebar.title("Selector de Gráficas")
    columna_elegida = st.sidebar.selectbox("Selecciona una columna", ['provincia','localidad','grupo_etario','semanas_epidemiologicas'])
    grafica_elegida = st.sidebar.selectbox("Selecciona una gráfica", ['lineplot', 'barras', 'dispersión'])

    # Generar la gráfica seleccionada
    if grafica_elegida == 'lineplot':
        if columna_elegida in ['provincia', 'localidad', 'grupo_etario']:
            fig, ax = plt.subplots()
            sns.lineplot(x=columna_elegida, y='cantidad_casos', data=df)
            plt.xticks(rotation=90)  # Rotación de 90 grados en las etiquetas del eje x        
            st.pyplot(fig)
        else:
            st.error("La columna seleccionada no es válida para esta gráfica.")
    elif grafica_elegida == 'barras':
        if columna_elegida in ['provincia', 'localidad', 'grupo_etario']:
            fig, ax = plt.subplots()
            sns.barplot(x=columna_elegida, y='cantidad_casos', data=df)
            plt.xticks(rotation=90)  # Rotación de 90 grados en las etiquetas del eje x        
            st.pyplot(fig)
        else:
            st.error("La columna seleccionada no es válida para esta gráfica.")
    elif grafica_elegida == 'dispersión':
        if columna_elegida in ['provincia', 'localidad', 'grupo_etario', 'semanas_epidemiologicas']:
            fig, ax = plt.subplots()
            sns.scatterplot(x=columna_elegida, y='cantidad_casos', data=df)
            plt.xticks(rotation=90)  # Rotación de 90 grados en las etiquetas del eje x
            st.pyplot(fig)
        else:
            st.error("La columna seleccionada no es válida para esta gráfica.")
        
