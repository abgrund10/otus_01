import socket
from urllib.parse import urlparse, parse_qs
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
    headers, body = string.split('\r\n\r\n')
    status_line, *headers = headers.split('\r\n')
    method, url, protocol = status_line.split()
    status = HTTPStatus(200)
    query = urlparse(url).query
    params = parse_qs(query)
    if 'status' in params:
        try:
            code = int(params['status'][0])
            status = HTTPStatus(code)
        except ValueError as error:
            resp_body = '\r\n'.join([
                f'Request Method: {method}',
                f'Request Source: {addr}',
                f'Response Status: {status}',
                *headers
            ])
    resp_headers = '\r\n'.join([
        f'{protocol} {status}',
        'Content-Type: text/plain',
        f'Content-Length: {len(resp_body)}'
    ])

    resp_msg = '\r\n\r\n'.join([
        resp_headers,
        resp_body
    ])
    conn.send(resp_msg.encode('utf-8'))

conn.close()
