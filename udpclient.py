from socket import *

# serverName = '10.143.217.160'
serverName = '10.143.15.196'

serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
message = 'a'
while message != 'q':
    message = input('Input lowercase sentence:')
    clientSocket.sendto(message.encode(), (serverName, serverPort))
    modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
    print(modifiedMessage.decode())
clientSocket.close()
