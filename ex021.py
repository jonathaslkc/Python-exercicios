import pygame

pygame.mixer.init()
pygame.mixer.music.load('ex021.mp3')
input(pygame.mixer.music.play())
pygame.event.wait()