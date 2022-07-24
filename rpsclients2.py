import socket

host = "192.168.194.5"
port = 2222


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))

while True:
    if(s.recv(100).decode("utf-8") == "connected"):
        print("You are connected")
        while True:
            msg = s.recv(16).decode("utf-8")
            print("...Rock Paper Scissor Game...\n Start Now")
            break
        if(msg == "wait"):
            print("Please wait...")
            while True:
                msg = s.recv(100).decode("utf-8")
                break
        if(msg == "start"):
            input =  input("rock, paper, or sciz\n choose 1: ")
            s.send(bytes(input,"utf-8"))
        while True:
            msg = s.recv(100).decode("utf-8")
            print(msg)
            while True:
                msg = s.recv(100).decode("utf-8")
                print(msg)
                break
            break
        break
    break
