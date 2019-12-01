import threading as thr
import socket
import time

def listening() :
    conn , client = s.accept()
    conns.append(conn)
    clients.append(client)

def disconnect_all():
    for client in clients:
        client.close()
    del conns[:] #Delete list items
    del clients[:]

def show_clients():
    while True:
        for client in clients:
            print(client)

def count ():
    for x in range(10):
        print (x)
        time.sleep(1)

HOST = "192.168.1.143"
PORT = 1883

conns = []
clients = []
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST,PORT)
s.bind(orig)
s.listen(1)

t1 = thr.Thread(target = listening)
t2 = thr.Thread(target = show_clients)

t1.start()
t2.start()



