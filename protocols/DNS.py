import socket
from dnslib import DNSRecord

class DNS:
    def __init__(self, domain_name, dns_server='8.8.8.8'):
        self.domain_name = domain_name
        self.dns_server = dns_server

    def send_dns_request(self):
        # Create a UDP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        # Set the DNS server IP address and port number
        dns_server = (self.dns_server, 53)

        # Create the DNS query message
        query_message = self.create_dns_query(self.domain_name)

        # Send the DNS query message to the DNS server
        sock.sendto(query_message, dns_server)

        # Receive the DNS response message from the DNS server
        response_message, _ = sock.recvfrom(4096)

        response_message = DNSRecord.parse(response_message)

        # Close the socket
        sock.close()

        return response_message

    def create_dns_query(self, domain_name):
        # Create a DNS query message for an A record
        query_id = 1234
        flags = 0x0100
        questions = 1
        answers = 0
        authority_rrs = 0
        additional_rrs = 0

        domain_parts = domain_name.split(".")
        qname = b""
        for part in domain_parts:
            length = len(part)
            qname += bytes([length])
            qname += part.encode()

        qtype = b"\x00\x01"  # A record type
        qclass = b"\x00\x01"  # IN class

        dns_query_message = (
                query_id.to_bytes(2, byteorder="big")
                + flags.to_bytes(2, byteorder="big")
                + questions.to_bytes(2, byteorder="big")
                + answers.to_bytes(2, byteorder="big")
                + authority_rrs.to_bytes(2, byteorder="big")
                + additional_rrs.to_bytes(2, byteorder="big")
                + qname
                + qtype
                + qclass
        )

        return dns_query_message


