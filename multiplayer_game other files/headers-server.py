#An intro using fixed length headers server
import socket

#Create a socket 
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((socket.gethostbyname(socket.gethostname()), 12345))
server_socket.listen()

message_1 = "Hello, we are learning more about sockets!"
message_2 = "Goodbye, now we know about headers!"

while True:
    #Accept connections
    client_socket, client_address = server_socket.accept()
    print(f"Connected to {client_address}\n")

    #Lets try to send two messages
    #client_socket.send(message_1.encode("utf-8"))
    #client_socket.send(message_2.encode("utf-8"))

    #Send two messages with headers of fixed length 10.
    #First create the header which will be of fixed ssize 10 and hold info about the size of the next message
    header = str(len(message_1))
    while len(header) < 10:
        header += " "

    #Now we have a header of size 10, we'll send the header followed by the message
    client_socket.send(header.encode("utf-8"))
    client_socket.send(message_1.encode("utf-8"))

    #Lets do the same thing for message2
    header = str(len(message_2))
    while len(header) < 10:
        header += " "

    client_socket.send(header.encode("utf-8"))
    client_socket.send(message_2.encode("utf-8"))