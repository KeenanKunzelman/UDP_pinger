# imports socket and configures it to recieve IPv4 UDP packets on port 5000
from socket import *
serverPort = 5000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))

# prompt the user ther server is up and ready to recieve
print('server is ready to revieve')

while True:
  #receive mesage and print it out
  message, clientAddress = serverSocket.recvfrom(2048)
  print(message)
  #capitalize the message and send it back to the client
  modifiedMessage = message.decode().upper()
  serverSocket.sendto(modifiedMessage.encode(), clientAddress)
