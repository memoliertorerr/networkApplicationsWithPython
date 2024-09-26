#An intro using fixed length headers client
import socket, time

#Create a socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((socket.gethostbyname(socket.gethostname()), 12345))

#Lets recieve two messages with a small bytesize of 8, will not work!!!
'''message = client_socket.recv(8)
print(message.decode("utf-8"))
message = client_socket.recv(8)
print(message.decode("utf-8"))'''

#Lets recieve two messages with a large bytesize of 1024, will work...for now! 
'''message = client_socket.recv(1024)
print(message.decode("utf-8"))
message = client_socket.recv(1024)
print(message.decode("utf-8"))'''

#what happens if we add some 'delay' time in between the client connecting and trying to recieve
'''time.sleep(2)
message = client_socket.recv(1024)
print(message.decode("utf-8"))
message = client_socket.recv(1024)
print(message.decode("utf-8"))
print("Why isn't this printing?!?!?!?!")'''

#We might not know the maximum byte size of the data being sent, it may be mre or less than 1024
#Two issues moving forward
#1) If our bytesize is too small, we might have issues not getting the full data packet
#2) If our bytesize is too large and there is a time delay between sending and recieving, we might 
#get more than one data packet being sent in a single .recv() call.

#We can fix this by ffirst recieving a HEADER of fixed length that will give the size of the incoming message packet.
time.sleep(2)
header = client_socket.recv(10)
print(header)   #We don't have to decode
print(len(header))
message = client_socket.recv(int(header))
print(message.decode("utf-8"))

time.sleep(2)
header = client_socket.recv(10)
print(header)  # We don't have to decode
print(len(header))
message = client_socket.recv(int(header))
print(message.decode("utf-8"))

print("Now this should print")