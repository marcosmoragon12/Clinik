# app.py
import streamlit as st

st.set_page_config(
    page_title="Clinik",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilos CSS avanzados para diseño de nivel profesional
st.markdown("""
<style>
    html, body, .main, .block-container {
        background-color: #ffffff !important;
        color: #1a1a1a !important;
        font-family: 'Inter', 'Segoe UI', sans-serif;
    }
    .main-title {
        font-size: 4rem;
        color: #143d3c;
        font-weight: 700;
        margin-bottom: 0.5rem;
        text-align: center;
    }
    .subtitle {
        font-size: 1.3rem;
        color: #495057;
        font-weight: 400;
        margin-bottom: 4rem;
        text-align: center;
    }
    .menu-box {
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 2rem;
        padding: 2rem 1rem 4rem;
    }
    .menu-item {
        background: #f8f9fa;
        border: 1.5px solid #b7c4c3;
        border-radius: 16px;
        padding: 1.8rem 2rem;
        width: 90%;
        max-width: 600px;
        text-align: center;
        font-size: 1.15rem;
        color: #143d3c;
        font-weight: 600;
        box-shadow: 0 4px 8px rgba(0,0,0,0.03);
        transition: all 0.2s ease-in-out;
        text-decoration: none;
    }
    .menu-item:hover {
        background-color: #e9ecef;
        transform: scale(1.015);
        cursor: pointer;
    }
    .footer-note {
        color: #6c757d;
        font-size: 0.9rem;
        margin-top: 4rem;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

# Título principal y eslogan
st.markdown("<div class='main-title'>Clinik</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Consultoría avanzada en análisis de datos y psicometría aplicada</div>", unsafe_allow_html=True)

# Menú visual como tarjetas con enlaces a módulos
st.markdown("<div class='menu-box'>", unsafe_allow_html=True)

modulos_ordenados = [
    ("📁 Exploración y Estadísticos Básicos", "0_Exploracion"),
    ("⚖️ Comparación de Grupos (t-test, ANOVA) (Próximamente)", None),
    ("🧪 Análisis Factorial Exploratorio (AFE)", "1_AFE"),
    ("📐 Análisis Factorial Confirmatorio (CFA) (Próximamente)", None),
    ("🤖 Modelos Predictivos y Machine Learning (Próximamente)", None),
    ("🧭 Segmentación y Clustering (Próximamente)", None)
]

for texto, ruta in modulos_ordenados:
    if ruta:
        st.markdown(f"<a href='/{ruta}' class='menu-item'>{texto}</a>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div class='menu-item'>{texto}</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# Pie de página informativo
st.markdown("""
<div class='footer-note'>📌 Usa el menú lateral izquierdo para acceder a los módulos disponibles.<br>🧪 Clinik está en desarrollo continuo — nuevos análisis se añadirán muy pronto.</div>
""", unsafe_allow_html=True)
