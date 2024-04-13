from socket import *

def reverse_sentence(sentence):
    words = sentence.split()
    reversed_sentence = ' '.join(reversed(words))
    return reversed_sentence

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print("The server is ready to receive!")
while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    message = message.decode()  # Decode received message
    modifiedMessage = reverse_sentence(message)  # Reverse sentence
    print('Received "' + message + '" and reversed to: "' + modifiedMessage + '"')
    serverSocket.sendto(modifiedMessage.encode(), clientAddress)
