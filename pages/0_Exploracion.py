# pages/0_Exploracion.py
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px
import io

st.set_page_config(page_title="Exploración de Datos", layout="wide")

# Estilos globales para fondo blanco constante y diseño profesional
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
    .step-card {
        background-color: #f1f3f5;
        padding: 1.2rem;
        border-radius: 10px;
        margin: 1rem 0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
</style>
""", unsafe_allow_html=True)

st.title("📁 Exploración y Estadísticos Básicos")

st.markdown("""
<div class='info-box'>
Clinik te permite cargar tu propia base de datos o generar una simulada según tus necesidades. Esta sección realiza una revisión exploratoria completa con gráficas y tablas de utilidad clínica. Ideal para informes, papers o evaluación preliminar de calidad de datos.
</div>
""", unsafe_allow_html=True)

# Paso 1: Carga o simulación
st.markdown("<div class='section-header'>Paso 1️⃣: Fuente de datos</div>", unsafe_allow_html=True)
col1, col2 = st.columns(2)
modo_datos = col1.radio("¿Cómo deseas comenzar?", ["📤 Subir mis datos", "🧪 Generar simulación"])

df = None
if modo_datos == "📤 Subir mis datos":
    archivo = col2.file_uploader("Carga un archivo .csv con tus datos clínicos", type="csv")
    if archivo is not None:
        df = pd.read_csv(archivo)
        st.success("✅ Datos cargados correctamente.")
else:
    with col2:
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
    st.markdown("<div class='section-header'>Paso 2️⃣: Exploración general</div>", unsafe_allow_html=True)

    with st.expander("🔍 Vista Previa del Dataset"):
        st.dataframe(df.head())

    with st.expander("📊 Estadísticos descriptivos"):
        st.write(df.describe().T.style.format("{:.2f}"))

    with st.expander("📉 Distribuciones por variable"):
        variables = st.multiselect("Selecciona variables para visualizar distribuciones:", df.columns, default=df.columns[:2])
        for var in variables:
            fig = px.histogram(df, x=var, marginal="box", nbins=30, title=f"Distribución de {var}", template="simple_white")
            st.plotly_chart(fig, use_container_width=True)

    with st.expander("📈 Matriz de correlaciones"):
        fig2, ax2 = plt.subplots(figsize=(10, 6))
        sns.heatmap(df.corr(), annot=True, fmt=".2f", cmap="Greens", ax=ax2)
        st.pyplot(fig2)

    with st.expander("🧩 Valores perdidos"):
        missing_count = df.isna().sum()
        if missing_count.sum() > 0:
            st.warning("⚠️ Hay valores perdidos en el dataset.")
            st.dataframe(missing_count[missing_count > 0])
        else:
            st.success("✅ No hay valores perdidos.")

    st.markdown("<div class='section-header'>Paso 3️⃣: Exportar datos preparados</div>", unsafe_allow_html=True)
    formato = st.selectbox("Formato de descarga", ["CSV", "Excel", "JSON"])
    nombre_archivo = st.text_input("Nombre del archivo a exportar", value="datos_explorados")

    if formato == "CSV":
        datos = df.to_csv(index=False).encode("utf-8")
        mime = "text/csv"
        file_name = f"{nombre_archivo}.csv"
    elif formato == "Excel":
        buffer = io.BytesIO()
        with pd.ExcelWriter(buffer, engine="xlsxwriter") as writer:
            df.to_excel(writer, index=False)
        datos = buffer.getvalue()
        mime = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        file_name = f"{nombre_archivo}.xlsx"
    else:
        datos = df.to_json(orient="records").encode("utf-8")
        mime = "application/json"
        file_name = f"{nombre_archivo}.json"

    st.download_button("💾 Descargar", data=datos, file_name=file_name, mime=mime)

else:
    st.info("Carga o genera un dataset para comenzar la exploración.")
