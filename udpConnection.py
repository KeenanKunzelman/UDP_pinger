#!/usr/bin/env python3

import socket
import time
from socket import *

message = "Hello dumb MAC"

def transmit(clientSocket,address,serverPort):
  clientSocket.settimeout(5) #set timeout for 5 seconds
  clientSocket.sendto(message.encode(), (address, serverPort))  #tranmitting from client to server

#tries to receive packet from server and handles timeout if server does not respond
  try:
    modifiedMessage, serverAddress = clientSocket.recvfrom(2048)  
    return True
  
  #packet timed out and was dropped
  except timeout:
    print("Packet was dropped")
    return False


def main():
  total_transmits = 0
  address = '137.142.175.107'
  serverPort = 5000
  totalTime = 0
  totalTimeouts=0

  # open the socket connection
  clientSocket = socket(AF_INET,SOCK_DGRAM)
  
  #only attempt to transmit 10 successful packets
  while total_transmits < 11:
  #check if 5 timeouts has been reached, then server is unreachable
    if totalTimeouts > 5: #ttl has been reached
      print("TTL is reached. Server is unreachable.")
      break
    start = time.time()  # start the timer for the round trip time

#tracks successful transmission
    if transmit(clientSocket,address,serverPort):
      end = time.time()
      #store total round trip transmission time
      totalTime += (end-start)
      print("Packet Recieved. Round trip time is :" + str(end-start))
  #timeout occured, add to count for 5 failed packets
    else:
      totalTimeouts+=1

      #calculate and print average transmission time
  print("Average time for the transmission is "+str(totalTime/10))

  clientSocket.close()  # closes the socket connection



if __name__ == "__main__":
  main()