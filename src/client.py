# echo-client.py

import socket

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
while True:
    message = input(" -> ")
    s.sendall(str(b"{message}").format(message=message))
    data = s.recv(1024).decode()
    print("Received: " + str(data))
    s.close()

#  valid input: "GET http://127.0.0.1/status=404 NotFound"
