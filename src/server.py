import socket
from urllib.parse import urlparse, parse_qs
from http import HTTPStatus

HOST = "127.0.0.1"
PORT = 65431

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen()
print(f"Server is started on {HOST}:{PORT}")
conn, addr = s.accept()
while True:
    data = conn.recv(1024)
    string = data.decode('utf-8')
    # headers, body = string.split('\r\n\r\n')
    # status_line, *headers = headers.split('\r\n')
    method, url, protocol = string.split()
    status = HTTPStatus(200)
    query = urlparse(url).query
    params = parse_qs(query)
    if 'status' in params:
        try:
            code = int(params['status'][0])
            status = HTTPStatus(code)
        except ValueError as error:
            pass

    response_headers = "Content-Type: text/html; charset=utf-8\n".encode("utf-8")
    conn.send(response_headers + f"Request Method: {method}\n"
                                 f"Request Source: ({HOST},{PORT})\n"
                                 f"Response Status: {status.value} {status.phrase}".encode("utf-8"))
conn.close()
