import socket
import re
from http import HTTPStatus

HOST = "127.0.0.1"
PORT = 65432

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen()
print(f"Server is started on {HOST}:{PORT}")
conn, addr = s.accept()
while True:
    data = conn.recv(1024)
    string = data.decode('utf-8')
    if not string:
        break
    value = re.split('status=', string)[1]
    method = string.split()[0]
    #   status_code = re.findall('[0-9]+', value)
    #   if status_code not in HTTPStatus:
    #       status_value = 200
    for status in HTTPStatus:
        if value == status:
            status_value = status.value
            status_phrase = status.phrase
            break
        else:
            status_value = HTTPStatus.OK
            status_phrase = HTTPStatus(HTTPStatus.OK).phrase

    response_headers = "Content-Type: text/html; charset=utf-8\n".encode("utf-8")
    conn.send(response_headers + f"Request Method: {method}\n"
                                 f"Request Source: ({HOST},{PORT})\n"
                                 f"Response Status: {status_value} {status_phrase}".encode("utf-8"))
conn.close()
