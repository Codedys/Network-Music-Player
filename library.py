import os

class Library:

    songs_list =[]
    

    def __init__(self,path):
        self.path = path
        for song in os.listdir(self.path):
            Library.songs_list.append(song)
        
        return Library.songs_list.pop([1])
    
    def next_song(self):
        return Library.songs_list.pop()
    
    



        