# 🚀 Sprint 7 – Descripción del proyecto

¡Felicidades! 🎉
Completaste la sección sobre herramientas de desarrollo de software. Ahora es el momento de aplicar los conocimientos y habilidades adquiridos al realizar un proyecto: **construir y desplegar un panel de control de una aplicación web en un servicio en la nube.**

Una vez que hayas terminado el proyecto, recuerda enviar tu trabajo al equipo de supervisión de proyectos para su evaluación.
👉 Recibirás una opinión en **48 horas**.
👉 Usa los comentarios para realizar cambios y luego envía la nueva versión al revisor.

Es normal recibir varios ciclos de retroalimentación ✅.
Tu proyecto se considerará **completado una vez que el revisor lo apruebe.**

---

## 🎯 Descripción del proyecto

El objetivo es que practiques tareas habituales de la ingeniería de software. Estas te ayudarán a complementar tus habilidades y a ser un candidato más atractivo para futuros empleadores.

Las tareas incluyen:

* Creación y gestión de **entornos virtuales de Python**.
* Desarrollo de una **aplicación web**.

En este proyecto se te da un dataset de **anuncios de venta de coches** (`vehicles_us.csv`), pero eres libre de elegir cualquier dataset en formato CSV.

👉 El análisis **no es el enfoque principal**. Lo que importa es crear y desplegar la aplicación web.

---

## 📝 Instrucciones para completar el proyecto

### 🔹 Paso 1. Configuración

1. Crea una cuenta en **GitHub** (si no la tienes).
2. Crea un nuevo repositorio con:

   * `README.md`
   * `.gitignore` (plantilla de Python).
3. Crea una cuenta en **Render.com** y vincúlala con tu GitHub.
4. Instala las librerías necesarias:

   ```bash
   pip install pandas plotly-express streamlit
   ```
5. Crea un entorno virtual, por ejemplo:

   ```
   vehicles_env
   ```
6. En el archivo `requirements.txt`, agrega las librerías sin versiones:

   ```
   pandas
   plotly_express
   streamlit
   ```
7. Clona tu repositorio en **VS Code** y configúralo con el intérprete de tu entorno virtual.

---

### 🔹 Paso 2. Descarga del archivo de datos

* Usa el dataset `vehicles_us.csv` o cualquier otro en formato CSV.
* Colócalo en el directorio del proyecto.

---

### 🔹 Paso 3. Análisis exploratorio de datos (EDA)

1. Crea un directorio:

   ```
   notebooks/
   ```
2. Crea un Jupyter Notebook `EDA.ipynb`.
3. Realiza algunas visualizaciones con `plotly-express`:

   * **Histograma**
   * **Gráfico de dispersión**

⚠️ No dediques demasiado tiempo al análisis. El foco está en la **aplicación web**.

---

### 🔹 Paso 4. Desarrollo del cuadro de mandos con Streamlit

1. Crea un archivo `app.py`.

2. Importa las librerías:

   ```python
   import pandas as pd
   import plotly.express as px
   import streamlit as st
   ```

3. Carga los datos en un DataFrame:

   ```python
   car_data = pd.read_csv('vehicles_us.csv')
   ```

4. Agrega componentes en Streamlit:

   * Un **encabezado** con `st.header()`
   * Un **botón para histograma**:

   ```python
   hist_button = st.button('Construir histograma')

   if hist_button:
       st.write('Creación de un histograma para los anuncios de coches')
       fig = px.histogram(car_data, x="odometer")
       st.plotly_chart(fig, use_container_width=True)
   ```

   * Un **botón para gráfico de dispersión**.
   * (Opcional) Sustituir botones por **checkboxes** con `st.checkbox()`.

5. Actualiza el `README.md` con:

   * Breve descripción del proyecto.
   * Funcionalidad principal de la app.

⚡ Ejecuta la app localmente:

```bash
streamlit run app.py
```

---

### 🔹 Paso 5. Despliegue en Render

1. En Render crea un **nuevo servicio web** vinculado a tu repo de GitHub.
2. Configuración:

   * **Build Command**:

     ```bash
     pip install --upgrade pip && pip install -r requirements.txt
     ```
   * **Start Command**:

     ```bash
     streamlit run app.py
     ```
3. Despliega y espera el build.
4. Accede a tu app en:

   ```
   https://<APP_NAME>.onrender.com/
   ```

   *(Nota: puede tardar unos minutos en despertar si está en plan gratuito).*

Para actualizar:
👉 "Manual Deploy" → "Latest Commit".

---

## 📤 ¿Cómo enviar mi proyecto?

* Envía el **enlace de tu repositorio en GitHub**.
* El repositorio debe ser **público**.

---

## 📊 ¿Cómo será evaluado?

El revisor verificará lo siguiente:

### ✅ Estructura mínima esperada

```
.
├── README.md
├── app.py
├── vehicles_us.csv
├── requirements.txt
└── notebooks
    └── EDA.ipynb
```

### ✅ Funcionalidad esperada

* Acceso a la aplicación web desde un navegador.
* Contenido mínimo en la app:

  * Encabezado con texto.
  * Al menos **un histograma**.
  * Al menos **un gráfico de dispersión**.
  * Al menos **un botón o checkbox**.

