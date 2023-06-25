import scapy.all as scapy
from scapy.layers.l2 import ARP as arp, Ether as ether


class ARP:
    def __init__(self, ip_address):
        self.ip_address = ip_address

    def send_arp_request(self):
        arp_request = arp(pdst=self.ip_address)
        broadcast = ether(dst="ff:ff:ff:ff:ff:ff")
        arp_request_broadcast = broadcast / arp_request
        answered_list = scapy.srp(arp_request_broadcast, timeout=5, verbose=False)[0]
        if answered_list:
            return f'MAC address: {answered_list[0][1].hwsrc}'
        else:
            return "No devices found."

