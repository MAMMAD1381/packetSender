import socket

TCP_IP = "127.0.0.1"
TCP_PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((TCP_IP, TCP_PORT))
sock.listen(1)
print(f'listening on {TCP_PORT}')
while True:
    conn, addr = sock.accept()
    print("Connection address:", addr)

    data = conn.recv(1024)
    print("received data:", data.decode())
    conn.send(data)  # echo

    conn.close()