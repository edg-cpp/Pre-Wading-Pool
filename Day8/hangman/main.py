import pygame
import functions

pygame.init()
screen = pygame.display.set_mode((600, 600))

ball = pygame.image.load("backround.jpg")
ballrect = ball.get_rect()


while True:
    # Process player inputs.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
        
        screen.fill("white")
        screen.blit(ball, ballrect)
        functions.draw_hangman(screen,(255,255,255))
        pygame.time.wait(3000)
        screen.fill("white")
        
        pygame.display.update()