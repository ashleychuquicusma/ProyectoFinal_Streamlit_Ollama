import requests


def consultar_ollama(
    pregunta,
    contexto,
    modelo="llama3.2",
    url="http://localhost:11434/api/generate",
):
    """Envía una pregunta a un modelo local de Ollama."""

    prompt = f"""
Eres un asistente especializado en análisis de datos.
Responde en español, de forma clara y basada en la información proporcionada.
Si la información no permite responder, indícalo sin inventar datos.

CONTEXTO DEL DATASET:
{contexto}

PREGUNTA DEL USUARIO:
{pregunta}
"""

    try:
        respuesta = requests.post(
            url,
            json={
                "model": modelo,
                "prompt": prompt,
                "stream": False,
            },
            timeout=120,
        )

        respuesta.raise_for_status()
        resultado = respuesta.json()

        return resultado.get(
            "response",
            "El modelo no devolvió una respuesta.",
        )

    except requests.exceptions.ConnectionError:
        return (
            "No se pudo conectar con Ollama. "
            "Comprueba que esté instalado y en ejecución."
        )

    except requests.exceptions.Timeout:
        return (
            "La consulta tardó demasiado. "
            "Inténtalo de nuevo."
        )

    except requests.exceptions.RequestException as error:
        return f"Error al consultar Ollama: {error}"
