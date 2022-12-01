import paho.mqtt.client as mqtt
import numpy as np
import librosa
import pyaudio
import wave 
import statistics

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    # Subscribing in on_connect() means that if we lose the connection and reconnect then subscriptions will be renewed.
    client.subscribe("ritalobo")

def on_message(client, userdata, msg):
    print("saving")
    print("")
    print("received message =" + str(msg.payload.decode()))
    main()
    print("")
    print("Done")

def main():
    # Record a few seconds of audio and save to a WAVE file.
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 2 
    RATE = 11025
    RECORD_SECONDS = 2 # valor que queremos 600
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
    data, fs = librosa.load('c:/Users/Rita Lobo/Documents/Rita Lobo/Universidade - Biomédica/5º ano/AAIB/projeto.wav')

    #Características extraídas
    
    #FFT
    
    n = len(data) # length of the signal
    k = np.arange(n)
    T = n/fs
    frq = k/T # two sides frequency range
    frq = frq[:len(frq)//2] # one side frequency range
    
    Y = np.fft.fft(data)/n # dft and normalization
    Y = Y[:n//2]
    
    #Frequência fundamental
    f0 = librosa.yin(data, fmin = librosa.note_to_hz('C2'), fmax= librosa.note_to_hz('C7'), sr = fs)
    
    FO_mean=[statistics.median(f0.tolist())]
    
    #soundwave é o sonograma em função do tempo
    sf_filewave = wave.open("c:/Users/Rita Lobo/Documents/Rita Lobo/Universidade - Biomédica/5º ano/AAIB/projeto.wav", 'r')
    signal_sf = sf_filewave.readframes(-1)
    soundwave_sf = np.frombuffer(signal_sf, dtype='int16')/len(data)

    # Converter áudio byters para inteiros
    soundwave_sf = np.frombuffer(signal_sf, dtype='int16')/len(data)

    # Sound Wave frame rate
    framerate_sf = sf_filewave.getframerate()
    
    # Encontrar os timestamps da sound wave 
    time_sf = np.linspace(start=0,
                        stop=len(soundwave_sf)/framerate_sf,
                        num=len(soundwave_sf))/2

    time1=time_sf.tolist()
    sound=soundwave_sf.tolist()

    a=[time1,sound]

    #RMSE
    y, fs = librosa.load('c:/Users/Rita Lobo/Documents/Rita Lobo/Universidade - Biomédica/5º ano/AAIB/projeto.wav')

    rmse = librosa.feature.rms(y=y)[0]
    time_rmse = librosa.times_like(rmse)

    time2=time_rmse.tolist()
    rmse_list=rmse.tolist()

    b=[time1, sound, time2, rmse_list]
    
    c=[time_sf.tolist(), soundwave_sf.tolist(), time_rmse.tolist(), rmse.tolist(), abs(Y).tolist(), frq.tolist(), FO_mean]

    client.publish("ritalobo22", str(c) )

    print("Acabei")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("mqtt.eclipseprojects.io", 1883, 60)
client.loop_forever()
