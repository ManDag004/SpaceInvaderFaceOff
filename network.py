import socket
import pickle


class Network:
    def __init__(self):
        self.clients = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "10.0.0.73"
        self.port = 5555
        self.addr = (self.server, self.port)
        self.player = self.connect()

    def getPlayer(self):
        return self.player

    def connect(self):
        try:
            self.clients.connect(self.addr)
            return pickle.loads(self.clients.recv(2048))
        except:
            pass

    def send(self, data):
        try:
            self.clients.send(pickle.dumps(data))
            return pickle.loads(self.clients.recv(2048))
        except socket.error as e:
            print(e)
