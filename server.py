import socket
import _thread
import sys
from main import read_pos, make_pos

server = "10.0.0.73"
port = 5555

# setup socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# try to bind socket to port
try:
    s.bind((server, port))
except socket.error as e:
    str(e)

# listen for connections (max 2)
s.listen(2)
print("Waiting for a connection, Server Started")

pos = [(0, 0), (100, 100)]

# function to run in background for each client 
def threaded_client(conn, player):
    conn.send(str.encode(make_pos(pos[player])))
    while True:
        try:
            # receive data from client
            data = read_pos(conn.recv(2048).decode())
            pos[player] = data

            # if data is empty
            if not data:
                print("Disconnected")
                break
            else:
                reply = pos[1 - player]
                print("Received:", data)
                print("Sending:", reply)
                reply = data

            # send data back to client
            conn.sendall(str.encode(make_pos(reply)))
        except:
            break
    
    # connection is lost
    print("Lost connection")
    conn.close()
    

# keeps server running
currentPlayer = 0
while True:
    conn, addr = s.accept()
    print("Connected to:", addr)

    _thread.start_new_thread(threaded_client, (conn, currentPlayer))
    currentPlayer += 1