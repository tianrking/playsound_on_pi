import pygame

pygame.init()
sound = pygame.mixer.Sound('/home/pi/Desktop/PlaySound/test.wav')
playing = sound.play()
while playing.get_busy():
    pygame.time.delay(100)
