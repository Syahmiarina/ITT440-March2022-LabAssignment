import socket

s = socket.socket()
print("Berjaya buat sokett")

port = 8888
<<<<<<< HEAD
=======

>>>>>>> b16bb9d (latest)
s.bind(('', port))
print("Berjaya bind soket di port: " + str(port))

s.listen(5)
print("soket tengah menunggu client!")

while True:
        c, addr = s.accept()
        print("Dapat capaian dari: " + str(addr))

<<<<<<< HEAD
        c.send(b'Terima Kasih!')
        buffer = c.recv(1024)
        print(buffer)
c.close()


=======
        c.send(b"Terima Kasih!")
        buffer = c.recv(1024)
        print(buffer)

c.close()
>>>>>>> b16bb9d (latest)
