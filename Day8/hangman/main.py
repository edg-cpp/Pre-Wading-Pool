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
        #tete
        pygame.draw.circle(screen,color=(0, 0, 0),center=[300, 150], radius=50,width=3)
        #corps
        pygame.draw.line(screen,color=(0,0,0),start_pos=[300,200],end_pos=[300,350],width=3)
        #jambes
        pygame.draw.line(screen,color=(0,0,0),start_pos=[300,350],end_pos=[200,450],width=3)
        pygame.draw.line(screen,color=(0,0,0),start_pos=[300,350],end_pos=[400,450],width=3)
        #bras
        pygame.draw.line(screen,color=(0,0,0),start_pos=[300,240],end_pos=[400,290],width=3)
        pygame.draw.line(screen,color=(0,0,0),start_pos=[300,240],end_pos=[200,290],width=3)
        
        pygame.display.update()