import paho.mqtt.client as mqtt
import numpy as np
import librosa
import librosa.display
import math
import speech_recognition as sr
import pyaudio
import wave
from pydub import AudioSegment  
import threading
from paho.mqtt import client as mqtt_client

# Receber a mensagem de start

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    # Subscribing in on_connect() means that if we lose the connection and reconnect then subscriptions will be renewed.
    client.subscribe("ritalobo")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

def subscribe():
    client.subscribe("ritalobo")
    client.on_message = on_message
    print("Subscribing")
    client.loop_forever()
    
client = mqtt_client.Client() 
client.on_connect = on_connect
client.connect("mqtt.eclipseprojects.io", 1883, 60)

#Subscrever ao tópico com loop forever para tentar encontrar o start
subscribe()


if client.subscribe("ritalobo", 1)  == "Start":
                
#Aqui no meio a parte de gravar e retirar características
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #Gravar o áudio
    # Record a few seconds of audio and save to a WAVE file.
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 44100
    RECORD_SECONDS = 10 # valor que queremos 600
    WAVE_OUTPUT_FILENAME = ("c:/Users/Rita Lobo/Documents/Rita Lobo/Universidade - Biomédica/5º ano/AAIB/projeto.wav")
    
    p = pyaudio.PyAudio()
    
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)
    
    print("* recording")
    
    frames = []
    
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)
    
    print("* done recording")
    
    stream.stop_stream()
    stream.close()
    p.terminate()
    
    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()
    
    # fazer load do ficheiro de som para data, com fs a frequência de aquisição
    data, fs = librosa.load('c:/Users/Rita Lobo/Documents/Rita Lobo/Universidade - Biomédica/5º ano/AAIB/projeto.wav',sr=44100)
    
    #Características extraídas
    #soundwave é o sonograma em função do tempo
    sf_filewave = wave.open("c:/Users/Rita Lobo/Documents/Rita Lobo/Universidade - Biomédica/5º ano/AAIB/projeto.wav", 'r')
    signal_sf = sf_filewave.readframes(-1)
    soundwave_sf = np.frombuffer(signal_sf, dtype='int16')/len(data)
    
    # Convert audio bytes to integers
    soundwave_sf = np.frombuffer(signal_sf, dtype='int16')/len(data)
    
    # Get the sound wave frame rate
    framerate_sf = sf_filewave.getframerate()
    
    # Find the sound wave timestamps
    time_sf = np.linspace(start=0,
                          stop=len(soundwave_sf)/framerate_sf,
                          num=len(soundwave_sf))/2
    
    #------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #MQTT
    client = mqtt.Client()
    #client.on_connect = on_connect
    client.connect("mqtt.eclipseprojects.io", 1883, 60)
    a = [time_sf, soundwave_sf]
    #a_bytearray = bytearray(b)
    client.publish("ritalobo", "aaaaaaaaaaaaaaaaaaaaa")
