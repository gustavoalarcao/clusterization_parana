import plotly.graph_objects as go
from pathlib import Path

from .constantes import w, h




downloads_path = Path.home() / "Downloads"

def baixar_grafico( 
        plot: go.Figure, 
        filename: str, 
        height: int=h, 
        width: int=w
) -> None:
    output_file = downloads_path / filename
    plot.write_image(output_file, height=height, width=width)
    


def mostrar_grafico(plot: go.Figure) -> None:
    plot.show(config={'staticPlot': True})
    