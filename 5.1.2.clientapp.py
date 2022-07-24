<<<<<<< HEAD
<<<<<<< HEAD
import socket

s = socket.socket()
=======
s = socket.socket(s = socket.socket(AF_INET, SOCK_STREAM, 0))
>>>>>>> 61fe425 (latest)
=======
import socket

s = socket.socket()
>>>>>>> 6a7d34b (lates)

port = 8888

s.connect(('192.168.194.5', port))

data = s.recv(1024)

s.send(b'Hi, saya client. Terima Kasih!');

print (data)

s.close()
<<<<<<< HEAD
<<<<<<< HEAD
=======

>>>>>>> 61fe425 (latest)
=======
>>>>>>> 6a7d34b (lates)
