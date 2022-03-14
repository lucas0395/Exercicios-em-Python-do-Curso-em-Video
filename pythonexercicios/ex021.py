# Faça um programa em python que abra e reproduza o áudio de arquivo em mp3

import pygame

# Inicializando o mixer PyGame
pygame.mixer.init()

# Iniciando o Pygame
pygame.init()

pygame.mixer.music.load('Despacito (Version Pop).mp3')
pygame.mixer.music.play(loops=0, start=0.0)
pygame.event.wait()

