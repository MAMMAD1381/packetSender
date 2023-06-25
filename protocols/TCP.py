import socket


class TCP:
    def __init__(self, ip_address, port, message):
        self.ip_address = ip_address
        self.port = port
        self.message = message
        pass

    def send_tcp_request(self):
        ip_address = self.ip_address
        port = int(self.port)
        message = self.message

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((ip_address, port))
        sock.sendall(message.encode())
        data = sock.recv(1024)
        sock.close()

        return data.decode()
