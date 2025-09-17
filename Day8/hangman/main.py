import pygame
import functions

pygame.init()
screen = pygame.display.set_mode((600, 600))

image = pygame.image.load("backround.jpg")
image_rect = image.get_rect()
screen.blit(image, image_rect)
functions.draw_hangman(screen,(255,255,255))

while True:
    # Process player inputs.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
    
    screen.blit(image, image_rect)

    pygame.display.flip()