import socket

port = 5000
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("127.0.0.1", port))

print("waiting on port:", port)

while True:
    try:
        data, addr = s.recvfrom(1024)
        print(str(data).split("'")[1])
        s.sendto(b"Hello, client!", addr)
    except Exception as error:
        print(error)




