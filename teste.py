import streamlit as st
import pandas as pd
import numpy as np
import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags,rc):
    print("Connected with result code" + str(rc))
    client.subscribe("AAIB/test")
    
def on_message(client, userdata, msg):
    print(msg.topic + "" + str(msg.payload))


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


st.write("Gráfico")

client=mqtt.Client()
client_on_connect= on_connect
client_on_message= on_message

client.connect("test.mosquitto.org", 1883, 60)
client.loop_forever()

chart_data = pd.DataFrame(
  np.random.randn(10,2),
  columns =[f"Col{i+1}" for i in range(2)]
)

st.line_chart(chart_data)

