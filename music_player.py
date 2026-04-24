import pygame
import random

pygame.mixer.init()

def start_music(file_path, mode):
    """Play a music file. Mode: '1' = loop, '2' = shuffle (later)."""
    pygame.mixer.music.load(file_path)

    if mode == "1":  # Loop
        pygame.mixer.music.play(-1)  # -1 means infinite loop
    else:
        pygame.mixer.music.play()  # Play once for now (shuffle later)

def stop_music():
    pygame.mixer.music.stop()