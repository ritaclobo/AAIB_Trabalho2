import streamlit as st
import time 
import pandas as pd
import numpy as np
import csv
import paho.mqtt.client as mqtt
from paho.mqtt import client as mqtt_client
import threading
from streamlit.runtime.scriptrunner.script_run_context import add_script_run_ctx


st.markdown(
    """ 
    <style>
    .header-style{
        font-size:25px;
        font-family:sans-serif;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """ 
    <style>
    .font-style{
        font-size:20px;
        font-family:sans-serif;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    '<p class="header-style"> Cloud Logger de Instrumentação </p>',
    unsafe_allow_html=True
)

#st.title("Cloud Logger de Instrumentação")

add_selectbox = st.sidebar.selectbox(
    "Escolher a característica?",
    ("Power", "Mean frequency", "Main frequency")
)

with st.sidebar:
    st.write("Projeto desenvolvido para a disciplina de Aplicações Avançadas de Instrumentação Biomédica.")
    st.write("O botão Start permite começar a gravação de som com o computador durante um certo número de segundos pré-definido.")
    st.write("Para acabar a aquisição pode carregar no botão de Stop.")
    add_radio = st.radio(
        "Escolher a característica",
        ("Power", "Mean frequency")
    )


st.write("Este primeiro gráfico represenda a amplitude da onda de som que foi gravada em função do tempo de gravação.")   
 
def plotd():
    df = pd.read_csv("teste_teste.csv", header=None)
    df.index = ["Tempo", "Sound Wave"]
    final_df=df.T
    st.line_chart(final_df, x = "Tempo", y="Sound Wave")

graph = st.empty;
plotd()

st.write("Gráfico")

chart_data = pd.DataFrame(
  np.random.randn(10,2),
  columns =[f"Col{i+1}" for i in range(2)]
)

st.line_chart(chart_data)
