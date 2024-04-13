from socket import *

def reverse_sentence(sentence):
    words = sentence.split()
    reversed_sentence = ' '.join(reversed(words))
    return reversed_sentence

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print('The server is ready to receive!')
while True:
    connectionSocket, addr = serverSocket.accept()
    message = connectionSocket.recv(1024).decode()
    modifiedMessage = reverse_sentence(message)
    print('Received "' + message + '" and reversed to: "' + modifiedMessage + '"')
    connectionSocket.send(modifiedMessage.encode())
    connectionSocket.close()
