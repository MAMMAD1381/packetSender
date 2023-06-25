# import socket
# import sys
#
# from icmplib import ping, multiping, traceroute, resolve
# from arprequest import ArpRequest
from protocols.TCP import TCP
from protocols.UDP import UDP
from protocols.ARP import ARP
from protocols.ICMP import ICMP
from protocols.DNS import DNS


class Client:
    def __init__(self):
        while True:
            selected_protocol = self.printMenu()
            match selected_protocol:
                case "1":  # ICMP
                    icmp = ICMP()
                    icmp.send_icmp_request()

                case "2":   # ARP
                    ip_address = input('pls enter the ip address\n')
                    arp = ARP(ip_address)
                    reply = arp.send_arp_request()
                    print(f'reply from ARP request to {ip_address} is: {reply}')

                case "3":   # UDP
                    udp = UDP()
                    udp.send_udp_request()

                case "4":   # TCP
                    tcp = TCP()
                    tcp.send_tcp_request()
                case "5":   # DNS
                    domain_name = input('pls enter dns domain:\n')
                    dns_server = input('pls enter the dns server (default: 8.8.8.8)\n')
                    dns = DNS(domain_name) if dns_server == '' else DNS(domain_name, dns_server)
                    response = dns.send_dns_request()
                    print(f'response from domain: {domain_name} with dns_server: {dns.dns_server} => {response}')
                case _:
                    self.printMenu()

    def printMenu(self):
        print('pls select a protocol')
        print(f'1.ICMP:'
              f'\n2.ARP:'
              f'\n3.UDP:'
              f'\n4.TCP:'
              f'\n5.DNS:')
        return input()

    # def ICMP(self, address):
    #     host = ping(address, count=4, interval=1, timeout=2, id=None, source=None, family=None, privileged=True)
    #     print(f'pinging {host.address} with average rtt: {host.avg_rtt} and {host.packet_loss} loss')
    #
    # def ARP(self, ip_address):
    #     ar = ArpRequest(ip_address, 'eth0')
    #     ar.request()
    #
    #
    # def UDP(self, ip_address, port):
    #
    #     # UDP_IP = "127.0.0.1"
    #     # UDP_PORT = 5005
    #     MESSAGE = "Hello, World!"
    #
    #     print ("UDP target IP:", ip_address)
    #     print ("UDP target port:", port)
    #     print ("message:", MESSAGE)
    #
    #     sock = socket.socket(socket.AF_INET,  # Internet
    #                          socket.SOCK_DGRAM)  # UDP
    #     sock.sendto(bytes(MESSAGE, "utf-8"), (ip_address, port))
    #
    # def TCP(self, ip_address, port):
    #
    #     data = " ".join(sys.argv[1:])
    #
    #     # Create a socket (SOCK_STREAM means a TCP socket)
    #     with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    #         # Connect to server and send data
    #         sock.connect((ip_address, port))
    #         sock.sendall(bytes(data + "\n", "utf-8"))
    #
    #         # Receive data from the server and shut down
    #         # received = str(sock.recv(1024), "utf-8")
    #
    #     print("Sent:     {}".format(data))
    #     # print("Received: {}".format(received))
    #
    # def DNS(self):
    #     pass
