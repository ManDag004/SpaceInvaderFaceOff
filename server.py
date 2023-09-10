import socket
import _thread
import sys

server = "10.0.0.7"
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


# function to run in background for each client 
def threaded_client(conn):
    while True:
        try:
            # receive data from client
            data = conn.recv(2048).decode("utf-8")

            # if data is empty
            if not data:
                print("Disconnected")
                break
            else:
                print("Received:", data)
                reply = data

            # send data back to client
            conn.sendall(str.encode(reply))
        except:
            break
    
    # connection is lost
    print("Lost connection")
    conn.close()
    

# keeps server running
while True:
    conn, addr = s.accept()
    print("Connected to:", addr)

    _thread.start_new_thread(threaded_client, (conn, ))