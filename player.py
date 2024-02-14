import pygame

class Player:

    pygame.init()


    def __init__(self,song):
        self.song = song
        pygame.mixer.music.load(self.song)

    def play(self):
        pygame.mixer.music.play()

    def pause(self):
        pygame.mixer.music.pause()

        
    def resume(self):
        pygame.mixer.music.unpause()
    
    def stop(self):
        pygame.mixer.music.stop()


        