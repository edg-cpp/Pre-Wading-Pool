import pygame


def draw_hangman(screen, color):
    # tete
    pygame.draw.circle(screen, color, center=[300, 150], radius=50, width=3)
    # corps
    pygame.draw.line(screen, color, start_pos=[300, 200], end_pos=[300, 350], width=3)
    # jambes
    pygame.draw.line(screen, color, [300, 350], [200, 450], 3)
    pygame.draw.line(screen, color, [300, 350], [400, 450], 3)
    # bras
    pygame.draw.line(screen, color, [300, 240], [400, 290], 3)
    pygame.draw.line(screen, color, [300, 240], [200, 290], 3)
    # potance
    pygame.draw.line(screen, color, [300, 100], [300, 50], 3)
    pygame.draw.line(screen, color, [300, 50], [100, 50], 3)
    pygame.draw.line(screen, color, [100, 50], [100, 550], 3)
    pygame.draw.line(screen, color, [100, 550], [450, 550], 3)
