import socket
import time
import paho.mqtt.client as mqtt 

HOST = input("Digite o host:")          # Endereco IP do Servidor
PORT = 1883            # Porta que o Servidor esta

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)
s.bind(orig)
s.listen(1)
while True:
    con, cliente = s.accept()
    print ("Conectado por", cliente)
    while True:
        msg = con.recv(1024)
        if not msg: break
        print (msg)
        
        
    print ('Finalizando conexao do cliente', cliente)
    con.close()
