import pygame

def play_music(file_path):
 pygame.init()
 pygame.mixer.init()
 pygame.mixer.music.load(file_path)
 pygame.mixer.music.play()

# Usage
file_path = "music.mp3"
play_music(file_path)
