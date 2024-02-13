import os

class Library:

    songs_list =[]
    

    def __init__(self,path):
        self.path = path
        for song in os.listdir(self.path):
            Library.songs_list.append(song)
    
    def next_song(self):
        return Library.songs_list.pop()
    
    



        