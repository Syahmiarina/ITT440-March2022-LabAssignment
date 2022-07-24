import socket

host = '192.168.194.5'
port = 2004
BUFFER_SIZE = 1024
MESSAGE = input("tcpClientA:")

tcpClientA = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpClientA.connect((host, port))

while MESSAGE != 'exit':
    tcpClientA.send(MESSAGE.encode())
    data = tcpClientA.recv(BUFFER_SIZE).decode()
    print(" ClientA received data:", data)
    MESSAGE = input("tcpClientA:")

tcpClientA.close()
