import socket
import sys
import time
import math
import errno
from multiprocessing import Process


def process_start(s_sock):
    s_sock.send(str.encode('ONLINE CALCULATOR'))

    while True:
        data = s_sock.recv(2048)
        data=data.decode('utf-8')

        try:
            choice,num=data.split(" ",2)
        except:
            print("DATA DENIED")
            break


        if(choice=='LOG'):
          print("\n LOG operation:",num)
          num=float(num)
          ans=math.log(num)
        elif(choice=='SQRT'):
            print("\n Square Root operation:",num)
            num=float(num)
            ans=math.sqrt(num)
        elif(choice=='EXPO'):
            print("\n Exponential operation:",num)
            num=float(num)
            ans=math.exp(num)
        elif(choice=='EXIT'):
            break
        ansopr="\n Answer: %s\n"% str(ans)
        s_sock.sendall(str.encode(ansopr))
    s_sock.close()

if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("",8888))
    print("Listen to the client...")
    s.listen(3)
    try:
        while True:
            try:
                s_sock, s_addr = s.accept()
                p = Process(target=process_start, args=(s_sock,))
                p.start()

            except socket.error:

                print('got a socket error')

    except Exception as e:
            print('an exception occurred!')
            print(e)
            sys.exit(1)
    finally:
           s.close()
