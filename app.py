
import streamlit as st
from pathlib import Path
from src.llm_client import consultar_ollama
from src.data_loader import cargar_datos
from src.eda import (
    analizar_dataset,
    obtener_estadisticas,
    contar_calidad,
    obtener_correlaciones,
)
from src.visualizations import (
    grafico_distribucion_calidad,
    grafico_correlaciones,
)

st.set_page_config(
    page_title="Análisis de Calidad del Vino",
    page_icon="🍷",
    layout="wide"
)

st.title("🍷 Análisis de Calidad del Vino")
st.subheader("Proyecto Final Integrador")
st.write(
    "Exploración y análisis de datos físico-químicos "
    "relacionados con la calidad del vino tinto."
)

RUTA_DATOS = Path(__file__).parent / "data" / "winequality-red.csv"

if RUTA_DATOS.exists():
    df = cargar_datos(RUTA_DATOS)

    st.success("Dataset cargado correctamente.")

    st.header("📊 Resumen del dataset")

    col1, col2, col3 = st.columns(3)
    col1.metric("Registros", df.shape[0])
    col2.metric("Variables", df.shape[1])
    col3.metric("Valores nulos", int(df.isna().sum().sum()))

 

    st.header("🧪 Análisis exploratorio")

    resumen = analizar_dataset(df)

    col1, col2 = st.columns(2)
    col1.metric("Filas duplicadas", resumen["filas_duplicadas"])
    col2.metric("Variables analizadas", resumen["variables"])

    st.subheader("🍷 Distribución de la calidad")
    figura_calidad = grafico_distribucion_calidad(df)
    st.plotly_chart(figura_calidad, use_container_width=True)

    st.subheader("🔗 Correlaciones entre variables")
    figura_correlaciones = grafico_correlaciones(df)
    st.plotly_chart(figura_correlaciones, use_container_width=True)


else:
    st.error(
        "No se encontró winequality-red.csv. "
        "Comprueba que esté dentro de la carpeta data."
    )

st.divider()
st.caption("Proyecto desarrollado con Python, Pandas y Streamlit.")







st.divider()

st.header("🤖 Asistente de IA sobre la calidad del vino")
st.write(
    "Haz preguntas sobre el dataset y recibe respuestas "
    "de la inteligencia artificial local."
)

pregunta = st.text_input(
    "¿Qué deseas saber sobre los datos del vino?",
    placeholder="Ej.: ¿Qué significa la variable alcohol?"
)

if st.button("Consultar a la IA"):
    if pregunta.strip():
        with st.spinner("La IA está preparando la respuesta..."):
            contexto = (
                f"El dataset contiene {df.shape[0]} registros "
                f"y {df.shape[1]} variables.\n"
                f"Variables: {', '.join(df.columns)}\n"
                f"Estadísticas descriptivas:\n{df.describe().to_string()}"
            )

            respuesta = consultar_ollama(
                pregunta=pregunta,
                contexto=contexto
            )

        st.subheader("Respuesta de la IA")
        st.write(respuesta)
    else:
        st.warning("Escribe una pregunta antes de consultar.")
