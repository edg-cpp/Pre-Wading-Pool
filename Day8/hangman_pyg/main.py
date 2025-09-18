import pygame
import op_screen as ops  # l'affichage du début
import english_words
import texts as txt  # les affichages du text
import py_hangman as hng  # copie du code du jour 7
import string

pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Hangman")

image = pygame.image.load("sources/backround.jpg")
image_rect = image.get_rect()

word = hng.return_random(english_words.get_english_words_set(["web2"], lower=True))
hidden_word = hng.hidden(word)
penalties = 0
not_in_word = []
in_word = []
is_running = False
coor_comm = (300, 350)


# font=pygame.font.SysFont()
click = False

while True:
    screen.blit(image, image_rect)
    ops.opening_screen(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit

        if event.type == pygame.MOUSEBUTTONDOWN:
            click = True

        if click == True:
            screen.blit(image, image_rect)
            txt.initial_message(screen, (300, 20))
            txt.show_hidden_word(screen, hidden_word)

            if event.type == pygame.KEYDOWN:
                input = pygame.key.name(event.key)

                if input in not_in_word or event in in_word:
                    txt.repetition_error()

                if input not in string.ascii_letters:
                    txt.letter_error()

                else:
                    letter = input

        pygame.display.update()
