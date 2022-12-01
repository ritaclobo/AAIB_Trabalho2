import streamlit as st
import time 
import pandas as pd
import numpy as np
import csv
import paho.mqtt.client as mqtt
from paho.mqtt import client as mqtt_client
import threading
from streamlit.runtime.scriptrunner.script_run_context import add_script_run_ctx

st.title("Cloud Logger de Instrumentação")

st.subheader("Comunicação de dados adquiridos através do MQTT Broker")

with st.sidebar:
    st.write("Projeto desenvolvido para a disciplina de Aplicações Avançadas de Instrumentação Biomédica.")
    st.write("O botão Start permite começar a gravação de som com o computador durante um certo número de segundos pré-definido.")
    st.write("Escolher a característica:")
    checkbox_one = st.checkbox("Sonograma")
    checkbox_two = st.checkbox("RMSE")

def plotd():
    df = pd.read_csv("outro_teste2.csv", header=None)
    df.index = ["Tempo", "Sound Wave", "Tempo RMSE" ,"RMSE"]
    final_df=df.T
    st.line_chart(final_df, x = "Tempo", y="Sound Wave")

graph = st.empty;

if checkbox_one:
    st.write("Este primeiro gráfico represenda a amplitude da onda de som que foi gravada em função do tempo de gravação.")   
    plotd()

if checkbox_two:
    st.write("O segundo gráfico representa a Energia RMS")
    df = pd.read_csv("outro_teste2.csv", header=None)
    df.index = ["Tempo", "Sound Wave", "Tempo RMSE" ,"RMSE"]
    final_df=df.T
    st.line_chart(final_df, x = "Tempo RMSE", y="RMSE")
