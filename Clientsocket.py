import socket
from player import Player



sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = (socket.gethostname(),10000)
sock.connect(server_address)

print("Enter START to start music player")
print ("Enter STOP to stop music player")
print(server_address)
start_or_stop = input("")

try:      
        if start_or_stop == "START":
            sock.sendall(start_or_stop.encode('utf-8'))
        with open("sing.mp3",'wb') as f:
            while True:
                song = sock.recv(1024)
                if not song:
                     print("done")
                     break
                f.write(song)
                print("writing")  
        print("Song copied") 
        game = Player("sing.mp3")
        while True:
            print("Enter S to start song P to pause R to resume and ST to stop")
            cstart = input("")
            if cstart == "S":
                game.play()
            elif cstart == "P":
                game.pause()
            elif cstart == "R":
                game.resume()
            elif cstart == "ST":
                game.stop()
                break
finally:
        sock.close()
    


                
            
        

        

        
        
        



