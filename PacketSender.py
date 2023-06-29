from protocols.TCP import TCP
from protocols.UDP import UDP
from protocols.ARP import ARP
from protocols.ICMP import ICMP
from protocols.DNS import DNS


class PacketSender:
    def __init__(self):
        while True:
            selected_protocol = self.print_protocols()  # printing protocols to select

            match selected_protocol:
                case "1":  # ICMP
                    ip_address = input('pls enter the ip address: \n')
                    data = input('data to send: \n')
                    icmp = ICMP(ip_address, data)
                    try:
                        reply = icmp.send_icmp_request()
                        print(reply)
                    except Exception as error:
                        print(f'error sending ICMP request: ip_address: {ip_address}, data: {data}\n'
                              f'error: {error}')

                case "2":  # ARP
                    ip_address = input('pls enter the ip address: \n')
                    arp = ARP(ip_address)
                    try:
                        reply = arp.send_arp_request()
                        print(f'reply from ARP request to {ip_address} is: {reply}')
                    except Exception as error:
                        print(f'error sending ARP request: ip_address: {ip_address}\n'
                              f'error: {error}')

                case "3":  # UDP
                    ip_address = input('pls enter the ip address: \n')
                    port = input('pls enter the port number: \n')
                    message = input('pls enter the message you wish to send: \n')
                    udp = UDP(ip_address, port, message)
                    try:
                        udp.send_udp_request()
                        print(
                            f'udp message was successfully sent to ip address: {ip_address} with port: {port} => '
                            f'message: {message}')
                    except Exception as error:
                        print(f'error sending UDP request to {ip_address} on port:{port}\n'
                              f'error: {error}')

                case "4":  # TCP
                    ip_address = input('pls enter the ip address: \n')
                    port = input('pls enter the port number: \n')
                    message = input('pls enter the message you wish to send: \n')
                    tcp = TCP(ip_address, port, message)
                    try:
                        tcp.send_tcp_request()
                        print(
                            f'udp message was successfully sent to ip address: {ip_address} with port: {port} => '
                            f'message: {message}')
                    except Exception as error:
                        print(f'error sending TCP request to {ip_address} on port:{port}\n'
                              f'error: {error}')

                case "5":  # DNS
                    domain_name = input('pls enter dns domain: \n')
                    dns_server = input('pls enter the dns server (default: 8.8.8.8): \n')
                    dns = DNS(domain_name) if dns_server == '' else DNS(domain_name, dns_server)
                    try:
                        response = dns.send_dns_request()
                        print(f'response from domain: {domain_name} with dns_server: {dns.dns_server} => {response}')
                    except Exception as error:
                        print(f'error sending DNS request from domain: {domain_name} with dns-server: {dns_server}\n'
                              f'error: {error}')

                case _:
                    self.print_protocols()

    def print_protocols(self):
        print('pls select a protocol')
        print(f'1.ICMP:'
              f'\n2.ARP:'
              f'\n3.UDP:'
              f'\n4.TCP:'
              f'\n5.DNS:')
        return input()


if __name__ == "__main__":
    PacketSender()
