# pages/0_Exploracion.py
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import io

st.set_page_config(page_title="Exploración de Datos", layout="wide")

st.markdown("""
<style>
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
En esta sección puedes subir tu propio conjunto de datos clínicos para una exploración inicial automatizada. Si no tienes uno, puedes generar una base de datos simulada configurando las características que deseas analizar.
</div>
""", unsafe_allow_html=True)

# Subida de datos o simulación
modo_datos = st.radio("¿Cómo deseas comenzar?", ["📤 Subir mis datos", "🧪 Generar datos simulados"])

df = None
if modo_datos == "📤 Subir mis datos":
    archivo = st.file_uploader("Carga un archivo .csv con tus datos clínicos", type="csv")
    if archivo is not None:
        df = pd.read_csv(archivo)
        st.success("✅ Datos cargados correctamente.")

else:
    n_obs = st.slider("Número de pacientes", 30, 500, 100)
    n_vars = st.slider("Número de variables clínicas", 3, 15, 8)
    correlacion = st.slider("Correlación promedio entre variables", 0.0, 0.9, 0.3)
    np.random.seed(42)
    base = np.random.multivariate_normal(mean=np.zeros(n_vars),
                                         cov=(correlacion * np.ones((n_vars, n_vars)) + (1 - correlacion) * np.eye(n_vars)),
                                         size=n_obs)
    df = pd.DataFrame(base, columns=[f"Var{i+1}" for i in range(n_vars)])
    st.success("✅ Datos simulados generados.")

if df is not None:
    st.markdown("<div class='section-header'>🔎 Vista Previa</div>", unsafe_allow_html=True)
    st.dataframe(df.head())

    st.markdown("<div class='section-header'>📊 Estadísticos descriptivos</div>", unsafe_allow_html=True)
    st.write(df.describe().T.style.format("{:.2f}"))

    st.markdown("<div class='section-header'>📉 Distribuciones</div>", unsafe_allow_html=True)
    var_sel = st.selectbox("Selecciona una variable para visualizar su distribución", df.columns)
    fig1, ax1 = plt.subplots()
    sns.histplot(df[var_sel], kde=True, ax=ax1, color="#40916c")
    st.pyplot(fig1)

    st.markdown("<div class='section-header'>📈 Matriz de correlaciones</div>", unsafe_allow_html=True)
    fig2, ax2 = plt.subplots(figsize=(10, 6))
    sns.heatmap(df.corr(), annot=True, fmt=".2f", cmap="Greens", ax=ax2)
    st.pyplot(fig2)

    st.markdown("<div class='section-header'>🔍 Valores perdidos</div>", unsafe_allow_html=True)
    missing_count = df.isna().sum()
    st.dataframe(missing_count[missing_count > 0]) if missing_count.sum() > 0 else st.success("✅ No hay valores perdidos.")

    st.markdown("<div class='section-header'>📁 Exportar datos preparados</div>", unsafe_allow_html=True)
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button("💾 Descargar dataset como CSV", data=csv, file_name="datos_explorados.csv", mime="text/csv")
else:
    st.info("Carga o genera un dataset para comenzar la exploración.")
