import socket

ClientSocket = socket.socket()
port = 8888

print('Connecting...')
try:
    ClientSocket.connect(('192.168.194.5', port))
except socket.error as e:
    print(str(e))

Response = ClientSocket.recv(2048)
print(Response)
print("\nOperation that available is LOG , Square root, and Exponential\n\n")

while True:

    choice=input(" LOG - LOG \n SQRT - Square Root \n EXPO - Exponential \n EXIT - exit terminal \n Enter operation : ")
    if(choice=='LOG'):
        num=input(" Number:")
    elif(choice=='SQRT'):
        num=input(" Number:")
    elif(choice=='EXPO'):
        num=input(" Number:")
    elif(choice=='EXIT'):
        print(" connection terminated")
        break

    message=choice+" "+num
    ClientSocket.send(str.encode(message))
    Response = ClientSocket.recv(2048)
    print(Response.decode('utf-8'))

ClientSocket.close()

