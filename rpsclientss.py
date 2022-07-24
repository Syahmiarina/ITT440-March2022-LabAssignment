import socket
host = "192.168.194.5"
port = 2222

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))

while True:
    if(s.recv(100).decode("utf-8") == "connected"):
	#receive data from server that socket has connected
        print("You are connected")
        while True:
            msg = s.recv(100).decode("utf-8")
		#receive data from server the game start now
            print("...Rock Paper Scissor Game...\n Start Now")
            break
        if(msg == "wait"):
		#if the client is player 2 it will wait  player1 choose first
            print("Please wait...")
            while True:
		#continue loop to recieve start data from server  
                msg = s.recv(100).decode("utf-8")
                break
        if(msg == "start"): 
		#when the client receive start the user can start choose rock paper or scissor
            input = input("rock, paper, or sciz\n choose 1: ")
            s.send(bytes(input,"utf-8"))
        while True:
		#client will receive both of what the player has pick
            msg = s.recv(100).decode("utf-8")
            print(msg)
            while True:
		#client will receive either draw lose or win
                msg = s.recv(100).decode("utf-8")
                print(msg)
                break
            break
        break
    break
