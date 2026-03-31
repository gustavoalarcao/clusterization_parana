import pandas as pd
import numpy as np

from utils.constantes import *

import requests




def coletando_ocorrencias_de_desastres(filepath) -> pd.DataFrame:
    df = pd.read_csv(
        filepath, 
        sep=';', 
        thousands='.', 
        decimal=','
    )
    return df


def coletando_coordenadas_parana():
    url = "https://servicodados.ibge.gov.br/api/v3/malhas/estados/PR?formato=application/vnd.geo+json"
    pr_geo_json = requests.get(url).json()
    pr_geo_json['features'][0]['id'] = 'PR'
    return pr_geo_json


