import socket
from library import Library

#create a socket
#bind socket to host
#listen for incoming connections
#Accept incoming connections

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = (socket.gethostname(),10000)

sock.bind(server_address)

sock.listen(1)

path = "/home/gerald/Downloads/Music"

songs = Library(path)

while True:
    connection,client_address = sock.accept()

    try:
       
        print("connection to  ",client_address," sucess")

        while True:

           print("fucntion")



    finally:
        connection.close()



 






