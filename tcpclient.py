from socket import *

# serverName = '10.143.15.196'  # school IP address
serverName = '192.168.56.1'  # home IP address

serverPort = 12000

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
sentence = input('Input a sentence you want to reverse: ')  # Get user input
clientSocket.send(sentence.encode())
modifiedSentence = clientSocket.recv(1024)
print("Message was received and reversed to: " + modifiedSentence.decode())  # Print the reversed message received from the server
clientSocket.close()
