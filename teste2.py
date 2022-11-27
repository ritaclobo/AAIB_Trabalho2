import streamlit as st
import pandas as pd
import numpy as np
import paho.mqtt.client as mqtt

# The callback for when the client receives a CONNACK response from the server.

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("luisaraujo")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic)
    value = list(msg.payload)
    for i in range(len(value)):
        print(value[i])

def subscribe():
    client.subscribe(topic)
    client.on_message = on_message
    print("Subscribing")
    client.loop_forever()
        
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("mqtt.eclipseprojects.io", 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a manual interface.
client.loop_forever()

# Fazer run do subscribe ao mesmo tempo do streamlit
from streamlit.runtime.scriptrunner.script_run_context import add_script_run_ctx
    if "mqttThread" not in st.session_state:
        st.session_state.mqttThread = th.Thread(target=MQTT_TH)
    add_script_run_ctx(st.session_state.mqttThread)

st.session_state.mqttThread.start()

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

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


# Using object notation
add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Power", "Mean frequency", "Main frequency")
)

# Using "with" notation
with st.sidebar:
    add_radio = st.radio(
        "Choose a shipping method",
        ("Standard (5-15 days)", "Express (2-5 days)")
    )

st.button("Start", on_click= "run test.py", type="secondary", disabled=False)
    
st.write("Gráfico")

chart_data = pd.DataFrame(
  np.random.randn(10,2),
  columns =[f"Col{i+1}" for i in range(2)]
)
#chart_data = pd.DataFrame(
#  np.random.randn(10,2),
#  columns =[f"Col{i+1}" for i in range(2)]
#)

st.line_chart(chart_data)




