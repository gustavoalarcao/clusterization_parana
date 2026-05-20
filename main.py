"""
Visualização das análises de dados via Streamlit.

Este módulo provê uma interface para facilitar a visualização 
de operações em DataFrames e gráficos durante o desenvolvimento. 
A utilização do Streamlit permite uma prototipagem mais ágil 
em comparação com ambientes de Notebook tradicionais.
"""


import streamlit as st
from streamlit import session_state as ss

st.set_page_config(layout='wide')


import pandas as pd
import numpy as np


from core.coletando_dados import *
from core.analise_primaria import *

from utils.constantes import *
from utils.plotly_template import *
from utils.auxiliar_plotagem import *
from utils.mapa_parana import *



# Coleta inicial (2010 - 2024).

df_desastres = coletando_ocorrencias_de_desastres(arquivo_ocorrencia_desastres)
# df_desastres
# df_desastres.dtypes

df_desastres['Prejuízo Público'] = df_desastres['Prejuízo Público'].str.replace('R$', '')
df_desastres['Prejuízo Público'] = df_desastres['Prejuízo Público'].str.replace('.', '')
df_desastres['Prejuízo Público'] = df_desastres['Prejuízo Público'].str.replace(',', '.')

df_desastres['impacto proporcional a populacao'] = df_desastres['Pessoas Afetadas'] / df_desastres['População'] 

impacto_proporcional_a_populacao = df_desastres.groupby('Município')['impacto proporcional a populacao'].sum()
impacto_proporcional_a_populacao = impacto_proporcional_a_populacao.sort_values(ascending=False)
# Removendo cidades com impacto relativo mínimo.
impacto_proporcional_a_populacao = impacto_proporcional_a_populacao.replace([np.inf, -np.inf], np.nan).dropna()

norma = impacto_proporcional_a_populacao.sum()
impacto_normalizado = impacto_proporcional_a_populacao / norma
impacto_normalizado

mais_impactadas = impacto_normalizado[impacto_normalizado > 0.01]
grafico_de_barras_impacto_proporcional = gerando_grafico_de_barras_impacto_proporcional(mais_impactadas)
mostrar_grafico(grafico_de_barras_impacto_proporcional)


















