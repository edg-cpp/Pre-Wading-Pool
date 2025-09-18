import pygame

pygame.font.init()

# les fonts
font_15 = pygame.font.Font("sources/pixel.ttf", 15)
font_30 = pygame.font.Font("sources/pixel.ttf", 30)
font_50 = pygame.font.Font("sources/pixel.ttf", 50)
font_60 = pygame.font.Font("sources/pixel.ttf", 60)

# fond d'écran
image = pygame.image.load("sources/backround.jpg")
image_rect = image.get_rect()

# couleurs
white = (255, 255, 255)
red = (255, 0, 0)

# coordinates
centre = (300, 300)
centre_haut = (300, 200)
centre_bas = (300, 400)


def opening_screen(screen):
    intro1 = font_60.render("HANGMAN", True, white)
    intro2 = font_30.render("CLICK TO START", True, white)
    # intro3 = font_50.render("ESC TO QUIT", True, white)

    introRect1 = intro1.get_rect()
    introRect2 = intro2.get_rect()
    # introRect3 = intro3.get_rect()

    introRect1.center = centre_haut
    introRect2.center = centre
    # introRect3.center = centre_bas

    screen.blit(intro1, introRect1)
    screen.blit(intro2, introRect2)
    # screen.blit(intro3, introRect3)


def initial_message(screen):
    text = font_30.render("Please enter a letter: ", True, white)
    textRect = text.get_rect()
    textRect.center = centre_haut
    screen.blit(text, textRect)


def show_penalties(screen, pen):
    str = f"Penalties : {pen}"
    color_text = white
    if pen > 8:
        color_text = red
    text = font_15.render(str, True, color_text)
    textRect = text.get_rect()
    textRect.center = (300, 100)
    screen.blit(text, textRect)


def show_hidden_word(screen, hword):
    text = font_50.render(hword, True, white)
    textRect = text.get_rect()
    textRect.center = centre
    screen.blit(text, textRect)


def repetition_error(screen):
    text = font_30.render("You already guessed this", True, red)
    textRect = text.get_rect()
    textRect.center = centre_bas
    screen.blit(text, textRect)


def letter_error(screen):
    text = font_30.render("You must enter a letter", True, red)
    textRect = text.get_rect()
    textRect.center = centre_bas
    screen.blit(text, textRect)


def guessed_letters(screen, list, coor):
    font = pygame.font.Font("sources/pixely.ttf", 30)
    # il doit y avoir une meilleure maniere de faire ça
    str_guessed = ""
    for e in set(list):
        str_guessed += e + " "
    text = font_30.render(str_guessed, True, white)
    textRect = text.get_rect()
    textRect.center = coor
    screen.blit(text, textRect)


def win_text(screen, word):
    screen.blit(image, image_rect)
    text = font_50.render("YOU WON", True, red)
    str = "The word was:" + word
    text2 = font_30.render(str, True, white)
    textRect = text.get_rect()
    text2Rect = text2.get_rect()
    textRect.center = centre_haut
    text2Rect.center = centre
    screen.blit(text, textRect)
    screen.blit(text2, text2Rect)


def lose_text(screen, word):
    screen.blit(image, image_rect)
    text = font_50.render("You Lost :(", True, red)
    str = "The word was:" + word
    text2 = font_30.render(str, True, white)
    textRect = text.get_rect()
    text2Rect = text2.get_rect()
    textRect.center = centre_haut
    text2Rect.center = centre
    screen.blit(text, textRect)
    screen.blit(text2, text2Rect)


def print_check(screen, txt):
    text = font_30.render(txt, True, white)
    textRect = text.get_rect()
    textRect.center = (300, 500)
    screen.blit(text, textRect)
