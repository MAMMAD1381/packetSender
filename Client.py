import socket
import sys

from icmplib import ping, multiping, traceroute, resolve
from arprequest import ArpRequest


class Client:
    def __init__(self, ip_address, port):

        # s = socket.socket()
        # port = 3000
        # s.connect(('127.0.0.1', port))
        while True:
            selected_protocol = self.printMenu()
            match selected_protocol:
                case "1":
                    self.ICMP(ip_address)

                case "2":
                    self.ARP()

                case "3":
                    self.UDP(ip_address, port)

                case "4":
                    self.TCP(ip_address, port)

                case "5":
                    self.DNS()
                case _:
                    self.printMenu()
        # receive data from the server and decoding to get the string.
        #     print(s.recv(1024).decode())

    def printMenu(self):
        print('pls select a protocol')
        print(f'1.ICMP:'
              f'\n2.ARP:'
              f'\n3.UDP:'
              f'\n4.TCP:'
              f'\n5.DNS:')
        return input()

    def ICMP(self, address):
        host = ping(address, count=4, interval=1, timeout=2, id=None, source=None, family=None, privileged=True)
        print(f'pinging {host.address} with average rtt: {host.avg_rtt} and {host.packet_loss} loss')

    def ARP(self):
        ar = ArpRequest('127.0.0.1', 'eth0')
        ar.request()

        ar2 = ArpRequest('10.0.0.123', 'eth0')  # 10.0.0.123 doesen't exist
        ar2.request()


    def UDP(self, ip_address, port):

        # UDP_IP = "127.0.0.1"
        # UDP_PORT = 5005
        MESSAGE = "Hello, World!"

        print ("UDP target IP:", ip_address)
        print ("UDP target port:", port)
        print ("message:", MESSAGE)

        sock = socket.socket(socket.AF_INET,  # Internet
                             socket.SOCK_DGRAM)  # UDP
        sock.sendto(bytes(MESSAGE, "utf-8"), (ip_address, port))

    def TCP(self, ip_address, port):

        data = " ".join(sys.argv[1:])

        # Create a socket (SOCK_STREAM means a TCP socket)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            # Connect to server and send data
            sock.connect((ip_address, port))
            sock.sendall(bytes(data + "\n", "utf-8"))

            # Receive data from the server and shut down
            # received = str(sock.recv(1024), "utf-8")

        print("Sent:     {}".format(data))
        # print("Received: {}".format(received))

    def DNS(self):
        pass


