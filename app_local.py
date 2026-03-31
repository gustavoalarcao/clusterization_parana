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

# df[['População', 'Prejuízo Público']] = df[['População', 'Prejuízo Público']].astype('Float64')

# df['Impacto Proporcional'] = df['População'] / df['Pessoas Afetadas']

# padrao = df.groupby('Município')['Impacto Proporcional'].sum()
# print(padrao.head(10))


st.write(df.head(10))

st.write(df.dtypes)

