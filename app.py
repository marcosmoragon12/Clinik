# app.py
import streamlit as st

st.set_page_config(
    page_title="Clinik",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilos CSS profesionales para diseño visual moderno
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
    .menu-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
        gap: 2rem;
        max-width: 1000px;
        margin: auto;
        padding-bottom: 3rem;
    }
    .menu-card {
        background-color: #f8f9fa;
        border: 1.5px solid #cfd8dc;
        border-radius: 16px;
        padding: 1.8rem 1.5rem;
        text-align: left;
        transition: 0.3s ease;
        box-shadow: 0 3px 6px rgba(0,0,0,0.05);
    }
    .menu-card:hover {
        background-color: #e9ecef;
        transform: translateY(-4px);
        cursor: pointer;
    }
    .menu-card h3 {
        font-size: 1.2rem;
        color: #1b4332;
        margin-bottom: 0.3rem;
    }
    .menu-card p {
        font-size: 0.95rem;
        color: #495057;
        margin: 0;
    }
    .footer-note {
        text-align: center;
        color: #868e96;
        font-size: 0.9rem;
        margin-top: 3rem;
    }
</style>
""", unsafe_allow_html=True)

# Hero section
st.markdown("""
<div class='hero-section'>
    <div class='hero-title'>Clinik</div>
    <div class='hero-subtitle'>Consultoría avanzada en análisis de datos y psicometría</div>
    <div class='hero-tagline'>Explora tus datos clínicos, obtén análisis inteligentes, toma decisiones fundamentadas.</div>
</div>
""", unsafe_allow_html=True)

# Menú en tarjetas visuales con descripción
modulos_ordenados = [
    ("📁 Exploración y Estadísticos Básicos", "0_Exploracion", "Revisión inicial de los datos con gráficos e indicadores clave"),
    ("⚖️ Comparación de Grupos (t-test, ANOVA) (Próximamente)", None, "Pruebas para comparar variables entre grupos clínicos"),
    ("🧪 Análisis Factorial Exploratorio (AFE)", "1_AFE", "Identifica estructuras latentes en tus cuestionarios"),
    ("📐 Análisis Factorial Confirmatorio (CFA) (Próximamente)", None, "Evalúa modelos teóricos con indicadores de ajuste"),
    ("🤖 Modelos Predictivos y Machine Learning (Próximamente)", None, "Predice variables o clasifica pacientes con algoritmos avanzados"),
    ("🧭 Segmentación y Clustering (Próximamente)", None, "Detecta perfiles o grupos clínicos similares")
]

st.markdown("<div class='menu-grid'>", unsafe_allow_html=True)
for texto, ruta, descripcion in modulos_ordenados:
    if ruta:
        st.markdown(f"""
        <a href='/{ruta}' style='text-decoration: none;'>
            <div class='menu-card'>
                <h3>{texto}</h3>
                <p>{descripcion}</p>
            </div>
        </a>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div class='menu-card'>
            <h3>{texto}</h3>
            <p>{descripcion}</p>
        </div>
        """, unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# Pie de página informativo
st.markdown("""
<div class='footer-note'>
📌 Usa el menú lateral izquierdo o las tarjetas para acceder a los módulos.<br>
🔒 Clinik es una herramienta en evolución, ideal para investigación aplicada y entornos clínicos reales.
</div>
""", unsafe_allow_html=True)
