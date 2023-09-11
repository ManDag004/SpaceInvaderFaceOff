import socket

class Network:
    def __init__(self):
        self.clients = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "10.0.0.73"
        self.port = 5555
        self.addr = (self.server, self.port)
        self.pos = self.connect()

    def getPos(self):
        return self.pos

    def connect(self):
        try:
            self.clients.connect(self.addr)
            return self.clients.recv(2048).decode()
        except:
            pass
        
    def send(self, data):
        try:
            self.clients.send(str.encode(data))
            return self.clients.recv(2048).decode()
        except socket.error as e:
            print(e)
