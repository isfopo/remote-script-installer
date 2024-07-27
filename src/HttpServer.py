import socket
import threading


class HttpServer:
    def __init__(self, host="0.0.0.0", port=8080):
        self.host = host
        self.port = port
        self.server_thread = threading.Thread(target=self.run_server)
        self.server_thread.daemon = True
        self.server_socket = None

    def start(self):
        if self.server_socket is None:
            self.server_thread.start()

    def run_server(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(1)

        while True:
            client_socket, addr = self.server_socket.accept()
            print(
                f"Connection from {addr}"
            )  # Use log message or appropriate logging in practice
            request = client_socket.recv(1024)
            print(
                f"Request: {request.decode('utf-8')}"
            )  # Use log message or appropriate logging in practice

            # Simple HTTP response
            html_response = b"""\
HTTP/1.1 200 OK
Content-Type: text/html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Simple HTTP Server</title>
</head>
<body>
    <h1>Hello from the Python HTTP Server!</h1>
</body>
</html>
"""
            client_socket.sendall(html_response)
            client_socket.close()

    def stop(self):
        if self.server_socket:
            self.server_socket.close()
