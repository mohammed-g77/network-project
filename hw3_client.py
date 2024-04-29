
#Client:

from socket import *
import sys, time

def main():
    print("UDP Sender/Client")

    host_remote = "127.0.0.1" 
    port_remote = "19999"
    timeout = 2  
    bufferSize = 1024

    clientsocket = socket(family=AF_INET, type=SOCK_DGRAM)
    clientsocket.settimeout(timeout)
    port_remote = int(port_remote)
    repeat = 0

    while repeat < 10:
        repeat += 1
        data = "Mohammed Ghanem " + str(repeat)        print("sending message @ "+ str(time.asctime()) + " = number of seconds passed since epoch = " + str(time.time()))
        print("") 

        try:
            start = time.time()
            clientsocket.sendto(data.encode(), (host_remote, port_remote))
            message, address = clientsocket.recvfrom(bufferSize)
            end = time.time()
            print("RTT: ", end - start)
        except:
            print("Request timed out.")
            continue

    clientsocket.close()

if _name__=="__main_":
    main()
    
