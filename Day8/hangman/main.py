import pygame

pygame.init()
screen = pygame.display.set_mode((600, 600))

while True:
    # Process player inputs.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit