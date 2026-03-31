import plotly.graph_objects as go

from .constantes import *


template = go.layout.Template()
template.layout = dict(
    autosize=False,
    showlegend=False,

    xaxis=dict( 
        showgrid=False,
        zeroline=False,
        showline=True,
        mirror=True,

        title=dict(
            font=dict(
                size=14,
                color=color
            ),
            standoff=10,
        ),
        tickfont=dict(
            size=10,
            color=color
        ),

        gridcolor=color,
        linecolor=color,
    ),
    yaxis=dict(
        showgrid=False,
        zeroline=False,
        showline=True,
        mirror=True,

        title=dict(
            font=dict(
                size=14,
            ),
            standoff=10,
        ),
        tickfont=dict(
            size=10,
            color=color
        ),

        gridcolor=color,
        linecolor=color, 
    ),
    margin=dict(t=30,b=60,r=60,l=60),
    paper_bgcolor='white',
    plot_bgcolor='white',
    width=w,
    height=h,
)