import streamlit as st

st.set_page_config(page_title="Estadificación Cáncer de Vulva", layout="centered")

st.title("🔬 Clasificación y Tratamiento de Cáncer de Vulva")
st.markdown("Esta herramienta permite determinar el **estadio clínico (FIGO)** y su tratamiento basado en características clínicas.")

# --- Inputs del usuario
tamano_cm = st.number_input("📏 Tamaño del tumor (en cm)", min_value=0.0, step=0.1)
invasion_mm = st.number_input("🧬 Profundidad de invasión estromal (en mm)", min_value=0.0, step=0.1)

organos_vecinos = st.selectbox(
    "🧠 Invasión a órganos vecinos",
    ["Ninguno", "Vagina distal", "Uretra distal", "Ano", "Uretra proximal", "Vejiga", "Mucosa rectal", "Hueso pélvico"]
)

ganglios = st.radio("🦠 Ganglios inguinales/femorales afectados", ["No", "Sí"])
metastasis = st.radio("🌍 ¿Hay metástasis a distancia?", ["No", "Sí"])


# --- Lógica para clasificación FIGO
def estadificar_cancer_vulva(tamano_cm, invasion_mm, organos_vecinos, ganglios, metastasis):
    if metastasis == "Sí":
        return "FIGO IV B - Metástasis a distancia"
    
    if organos_vecinos in ["Uretra proximal", "Vejiga", "Mucosa rectal", "Hueso pélvico"]:
        return "FIGO IV A - Invasión a estructuras profundas"

    if ganglios == "Sí":
        return "FIGO III - Ganglios inguinales/femorales positivos"
    
    if organos_vecinos in ["Vagina distal", "Uretra distal", "Ano"]:
        return "FIGO II - Invasión a estructuras adyacentes sin ganglios"
    
    if tamano_cm <= 2 and invasion_mm <= 1:
        return "FIGO I A - Tumor ≤2cm e invasión ≤1mm"
    
    return "FIGO I B - Tumor >2cm o invasión >1mm sin ganglios"


# --- Lógica para tratamiento según estadio
def tratamiento_por_estadio(estadio):
    tratamientos = {
        "FIGO I A": "Escisión local amplia o vulvectomía parcial. Seguimiento estrecho.",
        "FIGO I B": "Vulvectomía radical + linfadenectomía inguinofemoral bilateral.",
        "FIGO II": "Cirugía radical + posible radioterapia adyuvante si márgenes comprometidos.",
        "FIGO III": "Cirugía + radioterapia inguinopélvica +/- quimioterapia (según ganglios).",
        "FIGO IV A": "Exenteración pélvica o tratamiento multimodal (radioquimio).",
        "FIGO IV B": "Tratamiento paliativo (radio, quimio, control del dolor)."
    }
    return tratamientos.get(estadio.split(" ")[0], "Tratamiento no disponible para este estadio.")


# --- Mostrar resultados
if st.button("📊 Calcular Estadio y Tratamiento"):
    estadio = estadificar_cancer_vulva(tamano_cm, invasion_mm, organos_vecinos, ganglios, metastasis)
    tratamiento = tratamiento_por_estadio(estadio)

    st.success(f"**Estadio clínico asignado:** {estadio}")
    st.info(f"**Tratamiento sugerido:** {tratamiento}")
