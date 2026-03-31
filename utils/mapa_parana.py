import plotly.graph_objects as go

from utils.plotly_template import template

from core.coletando_dados import *


def gerando_mapa_parana(geo_json) -> go.Figure:
    fig = go.Figure()

    fig.add_trace(
        go.Choroplethmapbox(
            geojson=geo_json,
            locations=['PR'],
            z=[1],
            colorscale=[[0, "#b87e7e"], [1, '#b87e7e']],
            showscale=False,
        )
    )

    fig.update_layout(
        template=template,
        mapbox=dict(
            style="white-bg",
            center=dict(
                lat=-24.5, 
                lon=-51.0
            ),
            zoom=5.5
        ),
        margin=dict(r=0, t=0, l=0, b=0)
    )

    return fig