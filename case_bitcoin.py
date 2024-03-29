# -*- coding: utf-8 -*-
"""Case_Bitcoin.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1j1ExeoOYoaSoZgjlVwytu_ZrruuOTw5Q
"""

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 
import plotly.express as px
import plotly.graph_objects as Dash

dados = pd.read_excel('Dados_Bitcoin.xlsx')
dados

# Setar o index
dados.set_index("Date", inplace=True)

# Gráfico de linhas 
fig = px.line(dados, y = 'Close')

# plotar 
fig.show()

media_movel = dados['Close'].rolling(5).mean()
media_tendencia = dados['Close'].rolling(30).mean()

# Criar dash 
figura = Dash.Figure()

# Primeiro Eixo
figura.add_trace(
    Dash.Scatter(
        x= dados.index,
        y=dados.Close,
        mode ='lines',
        name='Fechamento',
        marker_color='#F08080'
    )
)

# Segundo Eixo
figura.add_trace(
    Dash.Scatter(
        x= dados.index,
        y=media_movel,
        mode ='lines',
        name='Média Movel',
        marker_color='#9370DB'
    )
)

# Terceiro Eixo
figura.add_trace(
    Dash.Scatter(
        x= dados.index,
        y=media_tendencia,
        mode ='lines',
        name='Tendência',
        marker_color='#ADFF2F'
    )
)

# Ajustando o layout
figura.update_layout(
    
    title='Análise do Fechamento do Bitcoin',
    titlefont_size=20,

    xaxis = dict(
        title='Período',
        titlefont_size=14,
        tickfont_size=10),
    
    yaxis = dict(
        title='Preço Fechamento ($)',
        titlefont_size=14,
        tickfont_size=10
    ),
    # Parametros para Legenda 
    legend = dict(
        y=-0.2,
        x=-0.1  ,
        
    )
    )

