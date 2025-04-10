import random
from socket import *
serverName = "172.21.153.206" # input IP address
serverPort = 20000
# Create a UDP socket
serverSocket = socket(AF_INET, SOCK_DGRAM)
# Assign IP address and port nubmer to socket
serverSocket.bind((serverName, serverPort))
print ("The server is running on " + serverName)

while True:
    rand = random.randint(0, 10)
    # Receive the client packet along with the address it is coming from save as messsage
    message, clientAddress = serverSocket.recvfrom(1024)

    # Capitalize teh message from the client
    modifiedMessage = message.decode().upper() # decodes the recieved message and makes it upper case
    
    # If rand is less than 4, we consider the packet lost and do not respond
    if rand < 4:
        continue
    
    # Otherwise, the server responds
    serverSocket.sendto(modifiedMessage.encode(), clientAddress)