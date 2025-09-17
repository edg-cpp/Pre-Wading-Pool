import pygame

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
        
        
        screen.fill("black")
        screen.blit(ball, ballrect)
        pygame.display.flip()