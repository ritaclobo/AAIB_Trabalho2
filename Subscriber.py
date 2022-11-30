import paho.mqtt.client as mqtt
import time
import csv
import json
import numpy
import numpy as np 

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    # Subscribing in on_connect() means that if we lose the connection and reconnect then subscriptions will be renewed.
    client.subscribe("ritalobo22")

print("Antes do on_connect")
def on_message(client, userdata, msg):
    print("saving")
    print("")
    print("received message =" + str(msg.payload.decode()))
    print(msg.payload.decode("utf-8"))
    print("")
    #res = json.loads(msg.payload.decode()) #Retornar à lista
    #l20001=[np.array(res[0]),np.array(res[1])] #passar interiores para array
    #write_data(l20001)  #escrever em csv
    print("Done")

def write_data(a):
    numpy.savetxt("teste10.csv", a, delimiter=",")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("mqtt.eclipseprojects.io", 1883, 60)
client.loop_forever()
