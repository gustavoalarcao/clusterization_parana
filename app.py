"""
Visualização das análises de dados via Streamlit.

Este módulo provê uma interface para facilitar a visualização 
de operações em DataFrames e gráficos durante o desenvolvimento. 
A utilização do Streamlit permite uma prototipagem mais ágil e modular 
em comparação com ambientes de Notebook tradicionais.
"""


import streamlit as st
from streamlit import session_state as ss

st.set_page_config(layout='wide')


import pandas as pd
import numpy as np

from core.coletando_dados import *

from utils.constantes import *
from utils.plotly_template import *
from utils.auxiliar_plotagem import *




df = coletando_ocorrencias_de_desastres(arquivo_ocorrencia_desastres)

df

df.dtypes

df['Prejuízo Público'] = df['Prejuízo Público'].str.replace('R$', '')
df['Prejuízo Público'] = df['Prejuízo Público'].str.replace('.', '')
df['Prejuízo Público'] = df['Prejuízo Público'].str.replace(',', '.')


df['Impacto Proporcional à População'] = df['População'] / df['Pessoas Afetadas']

impacto_proporcional_a_populacao = df.groupby('Município')['Impacto Proporcional à População'].sum()

impacto_proporcional_a_populacao = impacto_proporcional_a_populacao.sort_values(ascending=False)

impacto_proporcional_a_populacao = impacto_proporcional_a_populacao.replace([np.inf, -np.inf], np.nan).dropna()

norma = impacto_proporcional_a_populacao.sum()

impacto_normalizado = impacto_proporcional_a_populacao / norma

impacto_normalizado
















