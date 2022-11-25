import paho.mqtt.client as mqtt

import numpy as np
import matplotlib.pyplot as np
import librosa
import librosa.display
import math
import speech_recognition as sr
import pyaudio
import wave
from pydub import AudioSegment  
from pydub.playback import play  
from pandas import DataFrame
import pandas as pd

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

data, fs = librosa.load('c:/Users/Rita Lobo/Documents/Rita Lobo/Universidade - Biomédica/5º ano/AAIB/projeto.wav',sr=44100)


sf_filewave = wave.open("c:/Users/Rita Lobo/Documents/Rita Lobo/Universidade - Biomédica/5º ano/AAIB/projeto.wav", 'r')
signal_sf = sf_filewave.readframes(-1)
soundwave_sf = numpy.frombuffer(signal_sf, dtype='int16')/len(data)



client=mqtt.Client()
client.on_connect = on_connect
client.connect("test.mosquitto.org",1883,60)

client.publish("AAIB/test",str(soundwave_sf))
