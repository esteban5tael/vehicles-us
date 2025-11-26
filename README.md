# 🚗 Análisis de Mercado de Vehículos - vehicles-us

## 📋 Descripción del Proyecto

Este proyecto es una aplicación web interactiva construida con **Streamlit** que analiza y visualiza datos del mercado de vehículos usados en Estados Unidos. Utiliza un dataset de anuncios de venta de coches para proporcionar insights sobre precios, condiciones, características y tendencias del mercado.

## ✨ Funcionalidad Principal

La aplicación ofrece un dashboard interactivo con las siguientes características:

### 1. **Visualizaciones Interactivas**
- **Histograma**: Distribución del odómetro en los vehículos, mostrando la frecuencia de vehículos por rango de millas
- **Gráfico de Dispersión**: Relación entre el precio y el odómetro, permitiendo identificar patrones de depreciación

### 2. **Controles Flexibles**
- Opción de usar **botones** o **checkboxes** para mostrar/ocultar visualizaciones
- Interfaz intuitiva y responsiva

### 3. **Estadísticas Generales**
- Total de vehículos en el dataset
- Precio promedio de los vehículos
- Odómetro promedio

## 🛠️ Requisitos

- Python 3.7+
- Librerías:
  - `pandas`: Manipulación y análisis de datos
  - `plotly-express`: Visualizaciones interactivas
  - `streamlit`: Framework web

## 📦 Instalación

1. **Crear un entorno virtual** (opcional pero recomendado):
```bash
python -m venv vehicles_env
source vehicles_env/Scripts/activate  # En Windows
# o
source vehicles_env/bin/activate      # En macOS/Linux
```

2. **Instalar dependencias**:
```bash
pip install -r requirements.txt
```

## 🚀 Uso

Para ejecutar la aplicación localmente:

```bash
streamlit run app.py
```

La aplicación se abrirá automáticamente en tu navegador en `http://localhost:8501`

## 📊 Análisis Exploratorio de Datos (EDA)

Se incluye un Jupyter Notebook `notebooks/EDA.ipynb` con:
- Exploración del dataset
- Limpieza y preparación de datos
- Análisis estadístico detallado
- Visualizaciones adicionales

Para ejecutar el notebook:
```bash
jupyter notebook notebooks/EDA.ipynb
```

## 📁 Estructura del Proyecto

```
.
├── README.md                    # Este archivo
├── requirements.txt             # Dependencias del proyecto
├── app.py                       # Aplicación principal de Streamlit
├── vehicles_us.csv              # Dataset de vehículos
└── notebooks/
    └── EDA.ipynb               # Análisis exploratorio de datos
```

## 💡 Características del Dataset

El dataset `vehicles_us.csv` contiene información sobre anuncios de venta de vehículos usados con las siguientes columnas:

- **price**: Precio del vehículo ($)
- **model_year**: Año del modelo
- **model**: Modelo del vehículo
- **condition**: Condición del vehículo (excelente, buena, como nueva, etc.)
- **cylinders**: Número de cilindros
- **fuel**: Tipo de combustible (gasolina, diésel, híbrido)
- **odometer**: Lectura del odómetro (millas)
- **transmission**: Tipo de transmisión (automática, manual)
- **type**: Tipo de vehículo (sedan, SUV, pickup, etc.)
- **paint_color**: Color de la pintura
- **is_4wd**: Si es tracción en las cuatro ruedas
- **date_posted**: Fecha de publicación del anuncio
- **days_listed**: Días que estuvo listado el anuncio

## 🔍 Insights Clave

- La mayoría de los vehículos tienen entre 0 y 200,000 millas de recorrido
- Existe una correlación negativa entre el odómetro y el precio
- Los vehículos con menor kilometraje tienden a tener precios significativamente más altos

## 📝 Notas

- El análisis se enfoca en la visualización interactiva de datos
- Ideal para explorar tendencias del mercado de vehículos usados
- Puede servir como base para modelos predictivos de precios

## 👤 Autor

Proyecto desarrollado como parte del Sprint 7 de análisis y desarrollo web.

## 📄 Licencia

Este proyecto es de código abierto y está disponible bajo licencia abierta.
