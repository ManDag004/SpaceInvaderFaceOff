import socket
import pickle
import subprocess

command = 'ifconfig | grep "inet " | grep -Fv 127.0.0.1 | awk \'NR==1 {print $2}\''

try:
    server = subprocess.check_output(command, shell=True, universal_newlines=True).strip()
    print("Server IP: ", server)
except Exception as e:
    print("Error: ", e)

class Network:
    def __init__(self):
        self.clients = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = server
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
