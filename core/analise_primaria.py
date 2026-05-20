import plotly.graph_objects as go
import pandas as pd

from utils.plotly_template import template


def gerando_grafico_de_barras_impacto_proporcional(s: pd.Series) -> go.Figure:
    fig = go.Figure()
    fig.add_trace(
        go.Bar(
            x=s.index,
            y=s.values,
        )
    )
    fig.update_layout(
        template=template,
        barcornerradius=15,
        title=dict(text='Impacto Proporcional ao Tamanho da População')
    )

    return fig
    
