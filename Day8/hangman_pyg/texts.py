import pygame

pygame.font.init()
font = pygame.font.Font("sources/pixely.ttf", 30)
font2 = pygame.font.Font("sources/pixely.ttf", 50)

image = pygame.image.load("sources/backround.jpg")
image_rect = image.get_rect()


def repetition_error(screen, coor):
    text = font.render("You already guessed this", True, (255, 0, 0))
    textRect = text.get_rect()
    textRect.center = coor
    screen.blit(text, textRect)


def letter_error(screen, coor):
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
    str_guess = str(list)
    text = font.render(str_guess, True, (0, 0, 0))
    textRect = text.get_rect()
    textRect.center = coor
    screen.blit(text, textRect)


# def wrong_guess(screen, coor, letter):
#    screen.blit(image, image_rect)
#    str = "The letter '" + letter + "' is not in the word"
#    text = font.render(str, True, (0, 0, 0))
#    textRect = text.get_rect()
#    textRect.center = coor
#    screen.blit(text, textRect)
#
#
# def right_guess(screen, coor):
#    screen.blit(image, image_rect)
#    str = "Way to go!!"
#    text = font.render(str, True, (0, 0, 0))
#    textRect = text.get_rect()
#    textRect.center = coor
#    screen.blit(text, textRect)


def win_text(screen, word):
    screen.blit(image, image_rect)
    text = font2.render("YOU WON", True, (255, 0, 0))
    str = "The word was:" + word
    text2 = font.render(str, True, (0, 0, 0))
    textRect = text.get_rect()
    text2Rect = text2.get_rect()
    textRect.center = (300, 200)
    text2Rect.center = (300, 400)
    screen.blit(text, textRect)
    screen.blit(text2, text2Rect)


def lose_text(screen, word):
    screen.blit(image, image_rect)
    text = font2.render("You Lost :(", True, (255, 0, 0))
    str = "The word was:" + word
    text2 = font.render(str, True, (0, 0, 0))
    textRect = text.get_rect()
    text2Rect = text2.get_rect()
    textRect.center = (300, 300)
    text2Rect.center = (300, 400)
    screen.blit(text, textRect)
    screen.blit(text2, text2Rect)


def show_penalties(screen, pen):
    font_pen = pygame.font.Font("sources/pixely.ttf", 15)
    str = f"Penalties : {pen}"
    text = font_pen.render(str, True, (0, 0, 0))
    textRect = text.get_rect()
    textRect.center = (300, 200)
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
