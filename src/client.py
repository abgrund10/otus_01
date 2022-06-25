# echo-client.py

import socket

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server

while True:
    s = socket.socket()
    s.connect((HOST, PORT))
    message = input(" -> ")
    #  s.sendall(str(b"{message}").format(message=message))
    s.sendall(message)
    data = s.recv(1024).decode()
    print("Received: " + str(data))
    s.close()
