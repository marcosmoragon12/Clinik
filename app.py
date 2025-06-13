# app.py
import streamlit as st

st.set_page_config(
    page_title="Clinik",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilos CSS globales para fondo blanco fijo y diseño elegante
st.markdown("""
<style>
    html, body, .main, .block-container {
        background-color: #ffffff !important;
        color: #1c1c1c !important;
        font-family: 'Segoe UI', sans-serif;
    }
    .main-title {
        font-size: 3.5rem;
        color: #1b4332;
        margin-bottom: 0.2rem;
        text-align: center;
    }
    .subtitle {
        font-size: 1.2rem;
        color: #6b705c;
        font-weight: 400;
        margin-bottom: 3rem;
        text-align: center;
    }
    .menu-box {
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 1.5rem;
        padding: 1rem 0;
    }
    .menu-item {
        background-color: #ffffff;
        border: 2px solid #1b4332;
        border-radius: 10px;
        padding: 1.5rem 2rem;
        width: 500px;
        text-align: center;
        font-size: 1.1rem;
        color: #1b4332;
        font-weight: 500;
        transition: all 0.2s ease-in-out;
        text-decoration: none;
    }
    .menu-item:hover {
        background-color: #f4f4f4;
        cursor: pointer;
    }
    .footer-note {
        color: #7d7d7d;
        font-size: 0.9rem;
        margin-top: 3rem;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

# Título principal y eslogan
st.markdown("<div class='main-title'>Clinik</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Explora. Analiza. Comprende.</div>", unsafe_allow_html=True)

# Menú visualizado como tarjetas (el verdadero menú está en sidebar)
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

st.markdown("""
<div class='footer-note'>📌 Usa el menú lateral izquierdo para acceder a los módulos disponibles.</div>
""", unsafe_allow_html=True)
