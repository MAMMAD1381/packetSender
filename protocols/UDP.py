import socket


class UDP:
    def __init__(self, ip_address, port, message):
        self.ip_address = ip_address
        self.port = port
        self.message = message
        pass

    def send_udp_request(self):
        UDP_IP = self.ip_address
        UDP_PORT = int(self.port)
        MESSAGE = self.message

        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        message_bytes = MESSAGE.encode('utf-8')

        # Use the sendto method to send the message to the specified IP address and port
        # sock.sendto(message_bytes, (ip_address, port))
        sent = sock.sendto(message_bytes, (UDP_IP, UDP_PORT))
        return sent == len(MESSAGE)
