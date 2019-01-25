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

class Attiva_Disattiva_Zone:
    def __init__(self, zona1, zona2):
        self.AbZ1 = zona1
        self.AbZ2 = zona2

class Disattiva_Allarme:
    def __init__(self):
        self.Disatt = True

class Arduino:
    def __init__(self):
        self.s = socket.socket()
        host = socket.gethostname()
        port = 9100
        
        self.clients = []
        self.s.bind((host, port))
        self.s.listen(100)
        print("Socket in ascolto su porta ", port)
        _thread.start_new_thread(self.accettaConnessioniArduino, (1, 1))
        
    def accettaConnessioniArduino(self, a, b):
        while True:
            #Accetto Connessioni Client
            (c, addr) = self.s.accept()     
            print("Richiesta di connessione da ", addr)
            _thread.start_new_thread(self.onNewClient, (c, addr))

    #Quando un Arduino si autentica
    def onNewClient(self, clientsocket, addr):
        while True:
            msg = clientsocket.recv(1024)

            if msg.decode("utf-8").startswith("{") and msg.decode("utf-8").endswith("}"):
                print(msg)
                j = json.loads(msg)
                time.sleep(1)

                #if Devices.objects(mat = j['Seriale']):
                if True:
                    if "Seriale" in msg.decode("utf-8"):
                        t = Esito("OK")
                        trovato = False
                        rispondereOK = True
                        
                        for cl in self.clients:
                            if cl[1] == j['Seriale']:
                                trovato = True

                                cl[0] = clientsocket
                                print("Aggiornato Array")

                                try:
                                    cl[2] = j['Esito']
                                    rispondereOK = False
                                except:
                                    pass

                                try:
                                    x = j['Z1']
                                    rispondereOK = False
                                    cl[3] = msg.decode("utf-8")
                                except:
                                    pass

                                try:
                                    l = j['Log']
                                    rispondereOK = False
                                    print(l)
                                except:
                                    pass

                                break
                        
                        if not trovato:
                            self.clients.append([clientsocket, j['Seriale'], "", ""])
                            print("Aggiunto")

                        if rispondereOK:
                            clientsocket.send(bytearray(json.dumps(t.__dict__), 'utf-8'))
                        
                        print("NumClient ", len(self.clients))

                else:
                    t = Esito("KO")
                    clientsocket.send(bytearray(json.dumps(t.__dict__), 'utf-8'))
                    clientsocket.close()
                    break
            else:
                print ("msg Ignorato: " + msg.decode("utf-8"))


    def attivaZone(self, seriale, zona1, zona2):
        t = Attiva_Disattiva_Zone(zona1, zona2)
        
        for cl in self.clients:
            if cl[1] == seriale:
                cl[0].send(bytearray(json.dumps(t.__dict__), 'utf-8'))
                cl[2] = ""
                time1 = time.time()
                timeout = False
                while not timeout:
                    if cl[2] == "OK" or cl[2] == "KO":
                        return cl[2]
                    if time.time() > (time1 + 10):
                        print("Timeout")
                        timeout = True
        return "KO"

    def statoAllarme(self, seriale):
        for cl in self.clients:
            if cl[1] == seriale:
                cl[0].send(bytearray("STATO_ALLARME}", 'utf-8'))
                cl[3] = ""
                time1 = time.time()
                timeout = False
                while not timeout:
                    if cl[3] != "":
                        return cl[3]
                    if time.time() > (time1 + 10):
                        print("Timeout")
                        timeout = True
        return ""