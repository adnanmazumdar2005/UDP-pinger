from socket import *
import time

# Server details
serverName = "" # input server IP address
serverPort = 20000 # any port between 1024 and 65,535 (should match UDP_Pinger_Server port)

# UDP socket creation
clientSocket = socket(AF_INET, SOCK_DGRAM)

# server reply waiting time is set to 1 second, packet is considered lost if it exceeds 1 second
clientSocket.settimeout(1) 


message = input("Press Enter to start pinging") # press enter to start pinging the server
numberOfPings = int(input("Enter the number of pings you want to send"))

pings = 0
packetsLost = 0
rttList = []


# Ping ten times
for i in range(numberOfPings): # setting number of pings to be set
    
    sendTime = time.perf_counter() # records the time at which message is sent
    pingNumber = str(i + 1)
    message = f"ping {pingNumber} {sendTime}" 
    clientSocket.sendto(message.encode(), (serverName, serverPort))
    
    pings = pings + 1
    # clientSocket.sendto(message, "")
    
    try:
        message, address = clientSocket.recvfrom(1024)
        
        message = message.decode()
        
        recvTime = time.perf_counter() # records the time at which reply is recieved
        rtt = recvTime - sendTime
        rttList.append(rtt)
        print(f"Message received: {message}")
        print(f"Round Trip Time:{rtt} seconds")
        print()
    
    except timeout:
        print("Request timed out.")
        packetsLost = packetsLost + 1
        print()

packetsRecieved = pings - packetsLost
        
clientSocket.close()
        
print(f"Ping statistics for {serverName}:")
print(f"Packets: Sent = {pings}, Recieved = {packetsRecieved}, Lost = {packetsLost} ({(packetsLost/pings) * 100}% loss)")
print(f"Approximate round trip times in seconds: ")
print(f"Minimum = {min(rttList):.6f}seconds, Maximum = {max(rttList):.6f}seconds, Average = {(sum(rttList)/len(rttList)):.6f}seconds")       
print()
