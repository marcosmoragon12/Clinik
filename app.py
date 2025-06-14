# app.py
import streamlit as st

st.set_page_config(
    page_title="Clinik",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilos CSS profesionales con layout refinado
st.markdown("""
<style>
    html, body, .main, .block-container {
        background-color: #ffffff !important;
        color: #1a1a1a !important;
        font-family: 'Inter', 'Segoe UI', sans-serif;
    }
    .hero-section {
        background: linear-gradient(to right, #d8f3dc, #b7e4c7);
        padding: 4rem 2rem 3rem;
        border-radius: 12px;
        margin: 1rem auto 3rem;
        max-width: 1000px;
        box-shadow: 0 4px 16px rgba(0, 0, 0, 0.05);
        text-align: center;
    }
    .hero-title {
        font-size: 4rem;
        font-weight: 800;
        color: #1b4332;
        margin-bottom: 1rem;
    }
    .hero-subtitle {
        font-size: 1.4rem;
        font-weight: 400;
        color: #343a40;
        margin-bottom: 1rem;
    }
    .hero-tagline {
        font-size: 1rem;
        color: #6c757d;
    }
    .highlight-box {
        background-color: #f1f3f5;
        padding: 1.2rem 2rem;
        border-left: 4px solid #1b4332;
        border-radius: 8px;
        max-width: 800px;
        margin: 0 auto 2rem;
        font-size: 0.95rem;
        color: #343a40;
    }
    .modules-wrapper {
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
        gap: 2rem;
        max-width: 1100px;
        margin: 0 auto 2rem;
    }
    .module-card {
        flex: 1 1 300px;
        max-width: 320px;
        background-color: #f8f9fa;
        border-radius: 16px;
        border: 1.5px solid #d3d3d3;
        padding: 2rem 1.5rem;
        box-shadow: 0 4px 8px rgba(0,0,0,0.03);
        transition: 0.3s ease-in-out;
        text-align: center;
    }
    .module-title {
        font-size: 1.2rem;
        color: #1b4332;
        font-weight: 700;
        margin-bottom: 0.5rem;
    }
    .module-desc {
        font-size: 0.95rem;
        color: #495057;
        margin-bottom: 0.5rem;
    }
    .module-info-note {
        font-size: 0.8rem;
        color: #868e96;
        font-style: italic;
    }
    .footer-note {
        text-align: center;
        color: #868e96;
        font-size: 0.9rem;
        margin-top: 3rem;
    }
</style>
""", unsafe_allow_html=True)

# Sección Hero
st.markdown("""
<div class='hero-section'>
    <div class='hero-title'>Clinik</div>
    <div class='hero-subtitle'>Consultoría avanzada en análisis de datos y psicometría</div>
    <div class='hero-tagline'>Explora tus datos clínicos, obtén análisis inteligentes, toma decisiones fundamentadas.</div>
</div>
""", unsafe_allow_html=True)

# Caja de introducción destacada
st.markdown("""
<div class='highlight-box'>
🔬 Clinik hace accesible la estadística avanzada y la psicometría a profesionales de la salud, con herramientas prácticas y visualmente comprensibles.
</div>
""", unsafe_allow_html=True)

# Tarjetas de módulos SOLO informativas
modulos_ordenados = [
    ("📁 Exploración y Estadísticos Básicos", "0_Exploracion", "Revisión inicial de los datos con gráficos e indicadores clave"),
    ("⚖️ Comparación de Grupos (t-test, ANOVA)", None, "Próximamente: Pruebas para comparar variables entre grupos clínicos"),
    ("🧪 Análisis Factorial Exploratorio (AFE)", "1_AFE", "Identifica estructuras latentes en tus cuestionarios"),
    ("📐 Análisis Factorial Confirmatorio (CFA)", None, "Próximamente: Evalúa modelos teóricos con indicadores de ajuste"),
    ("🤖 Modelos Predictivos y Machine Learning", None, "Próximamente: Algoritmos para predicción clínica"),
    ("🧭 Segmentación y Clustering", None, "Próximamente: Agrupa perfiles clínicos similares")
]

st.markdown("<div class='modules-wrapper'>", unsafe_allow_html=True)
for texto, ruta, descripcion in modulos_ordenados:
    st.markdown(f"""
    <div class='module-card'>
        <div class='module-title'>{texto}</div>
        <div class='module-desc'>{descripcion}</div>
        <div class='module-info-note'>Disponible desde el menú lateral izquierdo</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# Pie de página informativo
st.markdown("""
<div class='footer-note'>
📌 Usa el menú lateral izquierdo para acceder a los módulos activos.<br>
🔒 Clinik evoluciona constantemente para convertirse en tu aliada profesional en investigación clínica y aplicada.
</div>
""", unsafe_allow_html=True)
