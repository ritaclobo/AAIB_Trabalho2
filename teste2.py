import streamlit as st
import time 
import pandas as pd
import numpy as np
import csv
import paho.mqtt.client as mqtt
from paho.mqtt import client as mqtt_client
import threading
from streamlit.runtime.scriptrunner.script_run_context import add_script_run_ctx

# MQTT

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    # Subscribing in on_connect() means that if we lose the connection and reconnect then subscriptions will be renewed.
    client.subscribe("ritalobo")

# The callback for when a PUBLISH message is received from the server.
#def on_message(client, userdata, msg):
#    print(msg.topic)
#    value = list(msg.payload)
#    for i in range(len(value)):
#        print(value[i])

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

def subscribe():
    client.subscribe("ritalobo")
    client.on_message = on_message
    print("Subscribing")
    client.loop_forever()
   

def mqtt_thread():
    for seconds in range(7):
            if 'mqttThread' not in st.session_state:
                st.session_state.mqttThread = threading.Thread(target=subscribe)
                add_script_run_ctx(st.session_state.mqttThread)
                st.session_state.mqttThread.start()
            time.sleep(1)
    del st.session_state['mqttThread']
    
client = mqtt_client.Client() 
client.on_connect = on_connect
client.connect("mqtt.eclipseprojects.io", 1883, 60)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Streamlit

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

if st.button("Start", key='start', type="secondary", disabled=False):
            client.publish("ritalobo",'Start')
            #placeholder2 = st.empty()
            mqtt_thread() 

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

st.write("Gráfico")


st.write(subscribe())
mqtt_thread() 


chart_data = pd.DataFrame(
  np.random.randn(10,2),
  columns =[f"Col{i+1}" for i in range(2)]
)

st.line_chart(chart_data)
with st.sidebar:
    st.write("Projeto desenvolvido para a disciplina de Aplicações Avançadas de Instrumentação Biomédica")
    add_radio = st.radio(
        "Escolher a característica",
        ("Power", "Mean frequency")
    )

st.write("Gráfico")

st.write(subscribe())
mqtt_thread() 

chart_data = pd.DataFrame(
  np.random.randn(10,2),
  columns =[f"Col{i+1}" for i in range(2)]
)

st.line_chart(chart_data)
