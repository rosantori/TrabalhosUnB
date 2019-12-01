import paho.mqtt.client as mqtt
import time

def on_connect(client, userdata, flags, rc):
    print("Connection status: ", connack_str(rc))


HOST = input("Digite o host:") #default
broker_port = 1883 #default

client = mqtt.Client()
client.connect(broker_host, broker_port)

client.subscribe("UMIDADE")
while True:
    if not msg: 
        break