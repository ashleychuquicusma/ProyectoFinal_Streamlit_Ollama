

\# Proyecto Final Integrador: Análisis de Calidad del Vino



\## 1. Descripción del proyecto



Aplicación web desarrollada con Python y Streamlit para explorar, analizar y visualizar datos relacionados con la calidad del vino tinto. Incluye un asistente de inteligencia artificial local mediante Ollama para responder preguntas sobre los resultados del análisis.



\## 2. Objetivo



Desarrollar una aplicación modular que permita cargar un dataset real, examinar sus variables, generar estadísticas y gráficos, e interpretar información mediante un modelo de inteligencia artificial local.



\## 3. Dataset



Se utiliza el dataset Wine Quality (vino tinto), publicado en el repositorio UCI Machine Learning Repository.



Fuente: https://archive.ics.uci.edu/dataset/186/wine+quality



El conjunto contiene 1599 registros y 12 variables, relacionadas con propiedades físico-químicas del vino y su calificación de calidad.



\## 4. Tecnologías utilizadas



\- Python

\- Streamlit

\- Pandas

\- NumPy

\- Plotly

\- Matplotlib

\- Seaborn

\- Scikit-learn

\- Requests

\- Ollama con el modelo llama3.2



\## 5. Estructura del proyecto



\- `app.py`: aplicación principal.

\- `data/`: archivos del dataset.

\- `src/data\_loader.py`: carga de datos.

\- `src/eda.py`: análisis exploratorio.

\- `src/visualizations.py`: gráficos.

\- `src/llm\_client.py`: conexión con Ollama.

\- `requirements.txt`: dependencias de Python.



\## 6. Instalación y ejecución



1\. Instalar Python.

2\. Instalar Ollama y descargar el modelo con:



&#x20;  `ollama pull llama3.2`



3\. Instalar las dependencias:



&#x20;  `pip install -r requirements.txt`



4\. Ejecutar la aplicación desde la carpeta del proyecto:



&#x20;  `python -m streamlit run app.py`



5\. Abrir en el navegador la dirección local que muestra Streamlit.



\## 7. Funcionalidades



\- Carga y vista previa del dataset.

\- Resumen de registros, variables y valores nulos.

\- Estadísticas descriptivas.

\- Análisis exploratorio de los datos.

\- Visualizaciones de la calidad y las correlaciones.

\- Asistente de IA local para responder preguntas sobre el dataset.



\## 8. Autora



Trabajo académico desarrollado como Proyecto Final Integrador.



