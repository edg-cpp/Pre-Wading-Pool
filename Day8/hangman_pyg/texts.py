import pygame

pygame.font.init()
font = pygame.font.Font("sources/pixel.ttf", 30)
font2 = pygame.font.Font("sources/pixel.ttf", 50)

image = pygame.image.load("sources/backround.jpg")
image_rect = image.get_rect()

main_color = (255, 255, 255)

# coordinates
centre = (300, 300)
centre_haut = (300, 200)
centre_bas = (300, 400)


def opening_screen(screen):
    font1 = pygame.font.Font("sources/pixel.ttf", 60)
    font2 = pygame.font.Font("sources/pixel.ttf", 30)

    intro1 = font1.render("HANGMAN", True, main_color)
    intro2 = font2.render("CLICK TO START", True, main_color)

    introRect1 = intro1.get_rect()
    introRect2 = intro2.get_rect()
    introRect1.center = centre_haut
    introRect2.center = centre

    screen.blit(intro1, introRect1)
    screen.blit(intro2, introRect2)


def initial_message(screen):
    text = font.render("Please enter a letter: ", True, main_color)
    textRect = text.get_rect()
    textRect.center = centre_haut
    screen.blit(text, textRect)


def show_penalties(screen, pen):
    font_pen = pygame.font.Font("sources/pixely.ttf", 15)
    str = f"Penalties : {pen}"
    text = font_pen.render(str, True, main_color)
    textRect = text.get_rect()
    textRect.center = (300, 100)
    screen.blit(text, textRect)


def show_hidden_word(screen, hword):
    text = font2.render(hword, True, main_color)
    textRect = text.get_rect()
    textRect.center = centre
    screen.blit(text, textRect)


def repetition_error(screen):
    text = font.render("You already guessed this", True, (255, 0, 0))
    textRect = text.get_rect()
    textRect.center = centre_bas
    screen.blit(text, textRect)


def letter_error(screen):
    text = font.render("You must enter a letter", True, (255, 0, 0))
    textRect = text.get_rect()
    textRect.center = centre_bas
    screen.blit(text, textRect)


def guessed_letters(screen, list, coor):
    font = pygame.font.Font("sources/pixely.ttf", 30)
    # il doit y avoir une meilleure maniere de faire ça
    str_guessed = ""
    for e in set(list):
        str_guessed += e + " "
    text = font.render(str_guessed, True, main_color)
    textRect = text.get_rect()
    textRect.center = coor
    screen.blit(text, textRect)


def win_text(screen, word):
    screen.blit(image, image_rect)
    text = font2.render("YOU WON", True, (255, 0, 0))
    str = "The word was:" + word
    text2 = font.render(str, True, main_color)
    textRect = text.get_rect()
    text2Rect = text2.get_rect()
    textRect.center = centre_haut
    text2Rect.center = centre_bas
    screen.blit(text, textRect)
    screen.blit(text2, text2Rect)


def lose_text(screen, word):
    screen.blit(image, image_rect)
    text = font2.render("You Lost :(", True, (255, 0, 0))
    str = "The word was:" + word
    text2 = font.render(str, True, main_color)
    textRect = text.get_rect()
    text2Rect = text2.get_rect()
    textRect.center = centre_haut
    text2Rect.center = centre
    screen.blit(text, textRect)
    screen.blit(text2, text2Rect)


def print_check(screen, txt):
    text = font.render(txt, True, main_color)
    textRect = text.get_rect()
    textRect.center = (300, 500)
    screen.blit(text, textRect)
