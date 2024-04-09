import pygame

def play_sound(file_path, repeat, channel):
    pygame.mixer.init()
    pygame.mixer.set_num_channels(100)
    pygame.mixer.Channel(channel).play(pygame.mixer.Sound(file_path), loops=repeat)