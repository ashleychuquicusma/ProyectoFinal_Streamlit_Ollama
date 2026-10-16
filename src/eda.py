import pandas as pd


def analizar_dataset(df):
    """Genera un resumen general del dataset."""

    resumen = {
        "registros": int(df.shape[0]),
        "variables": int(df.shape[1]),
        "valores_nulos": int(df.isna().sum().sum()),
        "filas_duplicadas": int(df.duplicated().sum()),
    }

    return resumen


def obtener_estadisticas(df):
    """Calcula estadísticas descriptivas de las variables numéricas."""

    return df.describe()


def contar_calidad(df):
    """Cuenta cuántos vinos hay para cada nivel de calidad."""

    return df["quality"].value_counts().sort_index()


def obtener_correlaciones(df):
    """Calcula la correlación entre las variables numéricas."""

    return df.corr(numeric_only=True)
