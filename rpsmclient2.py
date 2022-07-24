import socket

host ='192.168.194.5'
port = 2004
BUFFER_SIZE = 1024
MESSAGE = input("tcpClientB:")

tcpClientB = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpClientB.connect((host, port))

while MESSAGE != 'exit':
    tcpClientB.send(MESSAGE.encode())
    data = tcpClientB.recv(BUFFER_SIZE).decode()
    print(" ClientB received data:", data)
    MESSAGE = input("tcpClientB:")

tcpClientB.close()
