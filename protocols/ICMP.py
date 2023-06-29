import binascii
import os
import struct
import socket
import base64
import chardet


class ICMP:
    def __init__(self, ip_address, data=''):
        self.data = data
        self.ip_address = ip_address

    def send_icmp_request(self):
        # Create a raw socket
        icmp_socket = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)

        # Create the ICMP packet
        packet_id = os.getpid() & 0xFFFF
        packet_checksum = 0
        packet_header = struct.pack("bbHHh", 8, 0, packet_checksum, packet_id, 1)
        packet_data = bytes(self.data, 'utf-8')
        packet_checksum = self.calculate_checksum(packet_header + packet_data)
        packet_header = struct.pack("bbHHh", 8, 0, socket.htons(packet_checksum), packet_id, 1)
        packet = packet_header + packet_data

        # Send the ICMP request
        icmp_socket.sendto(packet, (self.ip_address, 1))

        # Wait for the response
        response_packet = icmp_socket.recv(1024)

        # Close the socket
        icmp_socket.close()

        return self.decoder(response_packet)

    def calculate_checksum(self, data):
        checksum = 0
        count_to = (len(data) // 2) * 2

        for count in range(0, count_to, 2):
            this_val = data[count + 1] * 256 + data[count]
            checksum += this_val
            checksum &= 0xffffffff

        if count_to < len(data):
            checksum += data[-1]
            checksum &= 0xffffffff

        checksum = (checksum >> 16) + (checksum & 0xffff)
        checksum += (checksum >> 16)
        result = ~checksum
        result &= 0xffff
        result = result >> 8 | (result << 8 & 0xff00)

        return result

    def decoder(self, encoded_str):

        icmp_type, code, checksum, packet_id, sequence = struct.unpack("bbHHh", encoded_str[:8])
        data = encoded_str[8:]

        try:
            decoded_data = data.decode('utf-8')
        except UnicodeDecodeError:
            encoding = chardet.detect(data)['encoding']
            decoded_data = data.decode(encoding)

        decoded_str = ''
        decoded_str += f"ICMP Type: {icmp_type}\n"
        decoded_str += f"Code: {code}\n"
        decoded_str += f"Checksum: {checksum}\n"
        decoded_str += f"Packet ID: {packet_id}\n"
        decoded_str += f"Sequence: {sequence}\n"
        decoded_str += f"Data: {decoded_data}\n"

        return decoded_str
