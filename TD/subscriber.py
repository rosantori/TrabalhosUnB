import paho.mqtt.client as mqtt

broker_host =  "192.168.0.169" #default
broker_port = 1883 #default

client = mqtt.Client()
client.connect(broker_host, broker_port)

client.subscribe("UMIDADE")
while True:
    if not msg: 
        break
