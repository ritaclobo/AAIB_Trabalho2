import streamlit as st
import time 
import pandas as pd
import numpy as np
import csv
import matplotlib.pyplot as plt
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
    st.write("Projeto desenvolvido para a disciplina de Aplicações Avançadas de Instrumentação Biomédica")
    add_radio = st.radio(
        "Escolher a característica",
        ("Power", "Mean frequency")
    )

def plotd():
    df = pd.read_csv("valores_test_csv")
    graph.line_chart(df.tail(10), x = "sample", y="valor")

graph = st.empty;


st.write("Gráfico")

chart_data = pd.DataFrame(
  np.random.randn(10,2),
  columns =[f"Col{i+1}" for i in range(2)]
)

st.line_chart(chart_data)
