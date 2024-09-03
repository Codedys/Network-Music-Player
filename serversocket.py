import socket
# from library import Library

#create a socket
#bind socket to host
#listen for incoming connections
#Accept incoming connections
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = (socket.gethostname(),10000)
sock.bind(server_address)
sock.listen(1)
path = "/home/jackson/Downloads/Anguka.mp3"

# songs = Library(path)
while True:
    connection,client_address = sock.accept()
    try:
        while True:
            data_input = connection.recv(1024).decode('utf-8')
            data_output = None
            if data_input == "START":
                # file = songs.next_song()
                print("connection to  ",client_address," sucess")
                with open (path,'rb') as f:
                    while True:
                        data_output = f.read(1024)
                        if not data_output:
                            print("Done")
                            break
                        connection.sendall(data_output)
                        print("sending.....................")
            elif data_input == "STOP":
                break               
    finally:
        connection.close()



 






