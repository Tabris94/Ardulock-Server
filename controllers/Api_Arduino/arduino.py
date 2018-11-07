from mongoengine import *
import socket
import _thread
import json
import time
import requests
from models.Devices import Devices

class Esito:
    def __init__(self, e):
        self.Esito = e

class Arduino:
    def __init__(self):
        Arduino.__instance = self
        self.s = socket.socket()
        host = socket.gethostname()
        port = 9100

        try:
            self.s.bind((host, port))
            self.s.listen(100)
            print("Socket in ascolto su porta ", port)
            _thread.start_new_thread(self.accettaConnessioniArduino, (1, 1))
        except: 
            print("Soket Gia Aperta")

    def accettaConnessioniArduino(self, a, b):
        while True:
            #Accetto Connessioni Client
            c, addr = self.s.accept()     
            print("Richiesta di connessione da ", addr)
            _thread.start_new_thread(self.onNewClient, (c, addr))

    #Quando un Arduino si autentica
    def onNewClient(self, clientsocket, addr):
        msg = clientsocket.recv(1024)
        print(msg)
        j = json.loads(msg)
        time.sleep(1)

        serial = Devices.objects(mat = j['Seriale'])
        if serial:
            t = Esito("OK")
        else:
            t = Esito("OK")

        clientsocket.send(bytearray(json.dumps(t.__dict__), 'utf-8'))
