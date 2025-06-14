# pages/0_Exploracion.py
import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import io
import random

st.set_page_config(page_title="Exploración de Datos", layout="wide")

# Estilos CSS
st.markdown("""
<style>
    html, body, .main, .block-container {
        background-color: #ffffff !important;
        color: #1a1a1a !important;
        font-family: 'Inter', 'Segoe UI', sans-serif;
    }
    .section-header {
        font-size: 1.5rem;
        font-weight: bold;
        color: #1b4332;
        margin-top: 2rem;
        margin-bottom: 1rem;
    }
    .info-box {
        background-color: #f8f9fa;
        border-left: 4px solid #1b4332;
        padding: 1rem;
        border-radius: 6px;
        margin-bottom: 1.5rem;
    }
</style>
""", unsafe_allow_html=True)

st.title("📁 Exploración y Estadísticos Básicos")

st.markdown("""
<div class='info-box'>
Crea o analiza tu base de datos para obtener una exploración clínica completa. Puedes subir un archivo .csv o definir variables personalizadas para simular un dataset clínico realista.
</div>
""", unsafe_allow_html=True)

modo_datos = st.radio("¿Cómo deseas comenzar?", ["📤 Subir mis datos", "🧪 Simular base personalizada"])
df = None

if modo_datos == "📤 Subir mis datos":
    archivo = st.file_uploader("Carga un archivo .csv", type="csv")
    if archivo is not None:
        df = pd.read_csv(archivo)
        st.success("✅ Datos cargados correctamente")

elif modo_datos == "🧪 Simular base personalizada":
    st.markdown("<div class='section-header'>📐 Configuración de variables</div>", unsafe_allow_html=True)
    n_obs = st.slider("Número de pacientes", 30, 500, 100)
    n_vars = st.number_input("Número de variables a crear", min_value=1, max_value=15, value=3, step=1)

    variable_definida = []
    for i in range(n_vars):
        with st.expander(f"🔧 Variable {i+1}"):
            nombre = st.text_input(f"Nombre de la variable {i+1}", value=f"Var{i+1}", key=f"nombre_{i}")
            tipo = st.selectbox("Tipo de variable", ["Cuantitativa", "Ordinal", "Nominal"], key=f"tipo_{i}")
            if tipo == "Cuantitativa":
                media = st.number_input("Media esperada", value=50.0, key=f"media_{i}")
                sd = st.number_input("Desviación estándar", value=10.0, key=f"sd_{i}")
                variable_definida.append((nombre, tipo, media, sd))
            elif tipo == "Ordinal" or tipo == "Nominal":
                n_cats = st.number_input("Número de categorías", min_value=2, max_value=10, value=3, key=f"cats_{i}")
                categorias = [st.text_input(f"Nombre categoría {j+1}", value=f"C{j+1}", key=f"cat_{i}_{j}") for j in range(n_cats)]
                variable_definida.append((nombre, tipo, categorias))

    if st.button("🚀 Generar base simulada"):
        simulada = {}
        for var in variable_definida:
            nombre = var[0]
            tipo = var[1]
            if tipo == "Cuantitativa":
                media, sd = var[2], var[3]
                simulada[nombre] = np.random.normal(loc=media, scale=sd, size=n_obs)
            else:
                categorias = var[2]
                simulada[nombre] = np.random.choice(categorias, size=n_obs)
        df = pd.DataFrame(simulada)
        st.success("✅ Datos simulados generados.")

if df is not None:
    st.markdown("<div class='section-header'>🔍 Vista previa y resumen</div>", unsafe_allow_html=True)
    st.dataframe(df.head())

    with st.expander("📊 Estadísticos descriptivos"):
        st.write(df.describe(include='all').T)

    with st.expander("📈 Distribuciones"):
        var_hist = st.selectbox("Selecciona una variable para ver su distribución:", df.columns)
        if df[var_hist].dtype == 'object':
            fig = px.histogram(df, x=var_hist, color=var_hist, title=f"Distribución de {var_hist}", template="simple_white")
        else:
            fig = px.histogram(df, x=var_hist, marginal="box", title=f"Distribución de {var_hist}", template="simple_white")
        st.plotly_chart(fig, use_container_width=True)

    with st.expander("📉 Matriz de correlación (solo numéricas)"):
        num_df = df.select_dtypes(include=np.number)
        if not num_df.empty:
            fig_corr, ax = plt.subplots(figsize=(10, 6))
            sns.heatmap(num_df.corr(), annot=True, cmap="Greens", ax=ax)
            st.pyplot(fig_corr)
        else:
            st.info("No hay variables numéricas suficientes para calcular correlaciones.")

    st.markdown("<div class='section-header'>📁 Exportar dataset</div>", unsafe_allow_html=True)
    nombre_archivo = st.text_input("Nombre del archivo", value="datos_explorados")
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button("💾 Descargar CSV", data=csv, file_name=f"{nombre_archivo}.csv", mime="text/csv")
else:
    st.info("Carga o genera un dataset para iniciar la exploración.")
