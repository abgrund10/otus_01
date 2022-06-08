import socket
import re
from http import HTTPStatus

HOST = "127.0.0.1"
PORT = 65432

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen()
conn, addr = s.accept()
print(f"Server is started on {HOST}:{PORT}")
while True:
    data = conn.recv(1024)
    string = str(data)
    if string.strip():
        value = re.split('status=', string)[1]
        print(value)
        method = string.split()[0]
        for status in HTTPStatus:
            if value == status:
                status_value = status.value
                status_phrase = status.phrase
                break
            else:
                status_value = HTTPStatus.OK
                status_phrase = HTTPStatus(HTTPStatus.OK).phrase

        response_headers = "Content-Type: text/html; charset=utf-8\n".encode("utf-8")
        conn.send(response_headers + f"Request Method: {method}"
                                     f"Request Source: ({HOST},{PORT})"
                                     f"Response Status: {status_value} {status_phrase}".encode("utf-8"))
        conn.close()
        break
    else:
        print("invalid input, please check")
