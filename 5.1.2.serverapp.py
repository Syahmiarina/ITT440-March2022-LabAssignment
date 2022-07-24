import socket
UDPs = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
print("Berjaya buat sokett")

port = 8888

UDPs.bind(('', port))
print("Berjaya bind soket di port: " + str(port))

UDPs.listen(5)
print("soket tengah menunggu client!")

while True:
        c, addr = UDPs.accept()
        print("Dapat capaian dari: " + str(addr))

        c.send(b"Terima Kasih!")
        buffer = c.recv(1024)
        print(buffer)

c.close()

