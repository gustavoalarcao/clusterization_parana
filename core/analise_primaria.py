import plotly.graph_objects as go
import pandas as pd

from utils.plotly_template import *


def gerando_grafico_de_barras_impacto_proporcional(s: pd.Series):
    fig = go.Figure()
    fig.add_trace(
        go.Bar(
            x=s.index,
            y=s.values,
        )
    )
    fig.update_layout(
        template=template,
        barcornerradius=15
    )
    return fig
    
