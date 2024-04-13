from socket import *

# serverName = '10.143.217.160'
# serverName = '10.143.15.196'  # school IP address
serverName = '192.168.56.1'  # home IP address

serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
message = None
while message != '!q':  # Loop until the user types '!q'
    message = input('Input lowercase sentence: ')  # Get user input
    if message == '!q':
        break  # Exit the loop before sending '!q' to the server
    clientSocket.sendto(message.encode(), (serverName, serverPort))
    modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
    print("Message was received and reversed to: " + modifiedMessage.decode())  # Print the reversed message received from the server
clientSocket.close()
