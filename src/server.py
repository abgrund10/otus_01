import socket
from urllib.parse import urlparse, parse_qs
from http import HTTPStatus

HOST = "127.0.0.1"
PORT = 65438


class serverConnection(object):
    def __init__(self, host, port):
        self._host = host
        self._port = port

    def __enter__(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((self._host, self._port))
        s.listen()
        self._s = s
        print(f"Server is started on {HOST}:{PORT}")
        return self._s

    def __exit__(self, *exc_info):
        if exc_info[0]:
            import traceback
            traceback.print_exception(*exc_info)
        self._s.close()


if __name__ == '__main__':
    with serverConnection(host=HOST, port=PORT) as s:
        while True:
            conn, addr = s.accept()
            data = conn.recv(1024)
            string = data.decode('utf-8')
            if not string:
                break
            # headers, body = string.split('\r\n\r\n')
            # status_line, *headers = headers.split('\r\n')
            try:
                method, url, protocol = string.split()
            except ValueError as error:
                method, url = string.split()
            status1 = HTTPStatus(200)
            query = urlparse(url).query
            params = parse_qs(query)
            if 'status' in params:
                try:
                    code = int(params['status'][0])
                    status1 = HTTPStatus(code)
                except ValueError as error:
                    status1 = HTTPStatus(200)
            status = status1

            response_headers = "Content-Type: text/html; charset=utf-8\n".encode("utf-8")
            conn.send(response_headers + f"Request Method: {method}\n"
                                         f"Request Source: ({HOST},{PORT})\n"
                                         f"Response Status: {status.value} {status.phrase}".encode("utf-8"))
            conn.close()
