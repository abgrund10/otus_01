# echo-client.py

import socket

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.sendall(b"GET http://127.0.0.1/status=404 NotFound")
data = s.recv(1024)
s.close()
print("Received: " + str(data))
