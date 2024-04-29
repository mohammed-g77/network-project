

# Server:
from socket import *
import sys, time

def main():
    print("UDP Receiver/Server")

    host_local = "127.0.0.1"
    port_local = "19999"
    bufferSize = 1024

    port_local = int(port_local)

    serverSocket = socket(family=AF_INET, type=SOCK_DGRAM)
    serverSocket.bind((host_local, port_local))

    print("UDP receiver starts listening (Waiting for connections)")

    while True:
        message, address = serverSocket.recvfrom(bufferSize)
        print("["+ str(time.asctime()) +"] received From:" + str(address[0]) + ":" +str(address[1])+ " : "  + message.decode() + ", hello!")

    serverSocket.close()

if _name__=="__main_":
    main()