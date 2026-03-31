import pandas as pd
import numpy as np

from utils.constantes import *

def coletando_ocorrencias_de_desastres(filepath) -> pd.DataFrame:
    df = pd.read_csv(filepath, sep=';')
    return df

