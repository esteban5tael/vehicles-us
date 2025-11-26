import pandas as pd
import plotly.express as px
import streamlit as st

# Cargar los datos
car_data = pd.read_csv('vehicles_us.csv')

# Encabezado de la aplicación
st.header('📊 Dashboard de Vehículos en Venta 🚗🚗🚗')

st.write("""
Análisis interactivo del mercado de vehículos usados en Estados Unidos.
Explore las características y tendencias de los anuncios de venta.
""")

# Separador
st.divider()

# Sección de visualizaciones
st.subheader('Visualizaciones')

# Opción de usar checkboxes en lugar de botones
use_checkboxes = st.checkbox('Usar checkboxes en lugar de botones', value=False)

st.divider()

if use_checkboxes:
    # Usar checkboxes
    show_histogram = st.checkbox('Mostrar Histograma')
    show_scatter = st.checkbox('Mostrar Gráfico de Dispersión')
else:
    # Usar botones
    col1, col2 = st.columns(2)
    
    with col1:
        show_histogram = st.button('Construir Histograma')
    
    with col2:
        show_scatter = st.button('Construir Gráfico de Dispersión')

st.divider()

# Histograma
if show_histogram:
    st.write('📈 Creación de un histograma para los anuncios de coches')
    fig_histogram = px.histogram(car_data, x="odometer", nbins=30,
                                 title='Distribución del Odómetro en Vehículos',
                                 labels={'odometer': 'Odómetro (millas)', 'count': 'Cantidad de Vehículos'})
    st.plotly_chart(fig_histogram, use_container_width=True)

# Gráfico de Dispersión
if show_scatter:
    st.write('📍 Creación de un gráfico de dispersión: Precio vs Odómetro')
    fig_scatter = px.scatter(car_data, x="odometer", y="price",
                             title='Relación entre Odómetro y Precio',
                             labels={'odometer': 'Odómetro (millas)', 'price': 'Precio ($)'},
                             opacity=0.6)
    st.plotly_chart(fig_scatter, use_container_width=True)

st.divider()

# Estadísticas adicionales
st.subheader('📋 Estadísticas Generales')
col1, col2, col3 = st.columns(3)

with col1:
    st.metric('Total de Vehículos', len(car_data))

with col2:
    st.metric('Precio Promedio', f'${car_data["price"].mean():.2f}')

with col3:
    st.metric('Odómetro Promedio', f'{car_data["odometer"].mean():.0f} millas')
