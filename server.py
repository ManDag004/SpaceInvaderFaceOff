import socket
import _thread
from player import Player
import pickle

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

players = [Player(0, 0, 100, 100, (255, 0, 0)), Player(100, 100, 100, 100, (0, 255, 0))]


# function to run in background for each client
def threaded_client(conn, player):
    conn.send(pickle.dumps(players[player]))
    while True:
        try:
            # receive data from client
            data = pickle.loads(conn.recv(2048))
            players[player] = data

            # if data is empty
            if not data:
                print("Disconnected")
                break
            else:
                reply = players[1 - player]
                print("Received:", data)
                print("Sending:", reply)

            # send data back to client
            conn.sendall(pickle.dumps(reply))
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
