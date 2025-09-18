import pygame

pygame.font.init()
font = pygame.font.Font("sources/pixely.ttf", 30)
font2 = pygame.font.Font("sources/pixely.ttf", 50)


def repetition_error(screen, coor):
    text = font.render("You already guessed this", True, (255, 0, 0))
    textRect = text.get_rect()
    textRect.center = coor
    screen.blit(text, textRect)


def letter_error(screen, coor):
    font = pygame.font.Font("sources/pixely.ttf", 30)
    text = font.render("You must enter a letter", True, (255, 0, 0))
    textRect = text.get_rect()
    textRect.center = coor
    screen.blit(text, textRect)


def initial_message(screen, coor):
    text = font.render("Please enter a letter: ", True, (0, 0, 0))
    textRect = text.get_rect()
    textRect.center = coor
    screen.blit(text, textRect)


def guessed_letters(screen, list, coor):
    font = pygame.font.Font("sources/pixely.ttf", 30)
    for e in list:
        str_guess += f"{e} "
    text = font.render(str_guess, True, (0, 0, 0))
    textRect = text.get_rect()
    textRect.center = coor
    screen.blit(text, textRect)


def wrong_guess(screen, coor, letter):
    str = "The letter '" + letter + "' is not in the word"
    text = font.render(str, True, (0, 0, 0))
    textRect = text.get_rect()
    textRect.center = coor
    screen.blit(text, textRect)


def wrong_guess(screen, coor):
    str = "Way to go!!"
    text = font.render(str, True, (0, 0, 0))
    textRect = text.get_rect()
    textRect.center = coor
    screen.blit(text, textRect)


def win_text(screen, coor, word):
    text = font2.render("YOU WON", True, (255, 0, 0))
    str = "The word was:" + word
    text2 = font.render(str, True, (0, 0, 0))
    textRect = text.get_rect()
    text2Rect = text2.get_rect()
    textRect.center = (300, 200)
    text2Rect.center = coor
    screen.blit(text, textRect)


def show_hidden_word(screen, hword):
    text = font2.render(hword, True, (0, 0, 0))
    textRect = text.get_rect()
    textRect.center = (300, 300)
    screen.blit(text, textRect)


def print(screen, txt):
    text = font.render(txt, True, (0, 0, 0))
    textRect = text.get_rect()
    textRect.center = (300, 500)
    screen.blit(text, textRect)
