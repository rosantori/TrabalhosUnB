import paho.mqtt.client as mqtt
import time

HOST = input("Digite o host:") #default
broker_port = 1883 #default

client = mqtt.Client()
client.connect(broker_host, broker_port)
f = open("data.txt")
while True:
    msg = f.readline()
    if not msg: break
    client.publish(topic = "UMIDADE", payload = msg[10:15], qos = 0, retain = False)
    client.publish(topic = "TEMPERATURA", payload = msg[31:36], qos = 0, retain = False)
    time.sleep(0.01)
f.close()
