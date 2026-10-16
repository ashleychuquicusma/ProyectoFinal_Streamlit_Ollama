from pathlib import Path
import pandas as pd


def cargar_datos(ruta=None):
    """Carga el dataset de calidad del vino tinto."""

    if ruta is None:
        raiz_proyecto = Path(__file__).resolve().parent.parent
        ruta = raiz_proyecto / "data" / "winequality-red.csv"

    ruta = Path(ruta)

    if not ruta.exists():
        raise FileNotFoundError(
            f"No se encontró el archivo de datos: {ruta}"
        )

    return pd.read_csv(ruta, sep=";")