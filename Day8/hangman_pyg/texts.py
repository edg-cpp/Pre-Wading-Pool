import pygame
import time

pygame.font.init()

# les fonts
pixel_15 = pygame.font.Font("sources/pixel.ttf", 15)
pixel_25 = pygame.font.Font("sources/pixel.ttf", 25)
pixel_30 = pygame.font.Font("sources/pixel.ttf", 30)
pixel_50 = pygame.font.Font("sources/pixel.ttf", 50)
pixel_60 = pygame.font.Font("sources/pixel.ttf", 60)

# fond d'écran
image = pygame.image.load("sources/backround.jpg")
image_rect = image.get_rect()

# couleurs
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)

# coordinates
centre_haut = (300, 200)
centre = (300, 300)
centre_bas = (300, 400)
centre_plus_bas = (300, 450)
bas = (300, 500)


def opening_screen(screen):
    intro1 = pixel_60.render("HANGMAN", True, white)
    intro2 = pixel_30.render("CLICK TO START", True, green)
    # intro3 = pixel_50.render("ESC TO QUIT", True, white)

    introRect1 = intro1.get_rect()
    introRect2 = intro2.get_rect()
    # introRect3 = intro3.get_rect()

    introRect1.center = centre_haut
    introRect2.center = centre
    # introRect3.center = centre_bas

    screen.blit(intro1, introRect1)

    # pour faire clignoter
    if time.time() % 1 > 0.5:
        screen.blit(intro2, introRect2)
    # screen.blit(intro3, introRect3)


def initial_message(screen):
    text = pixel_30.render("Please enter a letter: ", True, white)
    textRect = text.get_rect()
    textRect.center = centre_haut
    screen.blit(text, textRect)


def show_penalties(screen, pen):
    str = f"Penalties : {pen}"
    color_text = white
    if pen > 8:
        color_text = red
    text = pixel_15.render(str, True, color_text)
    textRect = text.get_rect()
    textRect.center = (300, 100)
    screen.blit(text, textRect)


def show_hidden_word(screen, hword):
    if len(hword) > 10:
        text = pixel_25.render("".join(hword), True, white)
    text = pixel_30.render("".join(hword), True, white)
    textRect = text.get_rect()
    textRect.center = centre
    screen.blit(text, textRect)


def repetition_error(screen):
    text = pixel_25.render("You already guessed this", True, red)
    textRect = text.get_rect()
    textRect.center = centre_bas
    screen.blit(text, textRect)


def letter_error(screen):
    text = pixel_25.render("You must enter a letter", True, red)
    textRect = text.get_rect()
    textRect.center = centre_bas
    screen.blit(text, textRect)


def guessed_letters(screen, letter_lst):
    letter_str = " ".join(letter_lst)

    if len(letter_str) > 10:
        letter_str2 = letter_str[10:]
        letter_str = letter_str[:10]
        text2 = pixel_30.render(letter_str2, True, white)
        text2Rect = text2.get_rect()
        text2Rect.center = bas
        screen.blit(text2, text2Rect)

    text = pixel_30.render(letter_str, True, white)
    textRect = text.get_rect()
    textRect.center = centre_plus_bas
    screen.blit(text, textRect)


def win_text(screen, word):
    screen.blit(image, image_rect)

    text = pixel_60.render("YOU WON", True, red)
    text2 = pixel_30.render("The word was: ", True, white)
    textw = pixel_50.render(str(word), True, white)

    textRect = text.get_rect()
    text2Rect = text2.get_rect()
    textwRect = textw.get_rect()

    textRect.center = centre_haut
    text2Rect.center = centre
    textwRect.center = centre_bas

    screen.blit(text, textRect)
    screen.blit(text2, text2Rect)
    screen.blit(textw, textwRect)


def lose_text(screen, word):
    screen.blit(image, image_rect)

    text = pixel_60.render("You Lost :(", True, red)
    text2 = pixel_30.render("The word was: ", True, white)
    textw = pixel_50.render(str(word), True, white)

    textRect = text.get_rect()
    text2Rect = text2.get_rect()
    textwRect = textw.get_rect()

    textRect.center = centre_haut
    text2Rect.center = centre
    textwRect.center = centre_bas

    screen.blit(text, textRect)
    screen.blit(text2, text2Rect)
    screen.blit(textw, textwRect)


def print_check(screen, txt):
    text = pixel_30.render(txt, True, white)
    textRect = text.get_rect()
    textRect.center = (300, 500)
    screen.blit(text, textRect)
