import plotly.express as px


def grafico_distribucion_calidad(df):
    """Crea un gráfico de barras de la calidad del vino."""

    conteo = (
        df["quality"]
        .value_counts()
        .sort_index()
        .rename_axis("Calidad")
        .reset_index(name="Cantidad")
    )

    figura = px.bar(
        conteo,
        x="Calidad",
        y="Cantidad",
        title="Distribución de la calidad del vino",
        labels={
            "Calidad": "Nivel de calidad",
            "Cantidad": "Número de vinos",
        },
    )

    figura.update_layout(
        xaxis_title="Nivel de calidad",
        yaxis_title="Número de vinos",
    )

    return figura


def grafico_correlaciones(df):
    """Crea un mapa de calor de las correlaciones."""

    correlaciones = df.corr(numeric_only=True)

    figura = px.imshow(
        correlaciones,
        text_auto=".2f",
        aspect="auto",
        title="Mapa de correlaciones entre variables",
        color_continuous_scale="RdBu_r",
        zmin=-1,
        zmax=1,
    )

    return figura
