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
            txt.show_penalties(screen, penalties)
            txt.guessed_letters(screen, not_in_word, (300, 500))

            if event.type == pygame.KEYDOWN:
                inp = pygame.key.name(event.key)

                if inp in not_in_word or inp in in_word:
                    txt.repetition_error(screen, coor_comm)

                if inp not in string.ascii_letters:
                    txt.letter_error(screen, coor_comm)

                else:
                    letter = inp
                    index = hng.find_letter(word, letter)
                    if index == False:
                        penalties += 1
                        not_in_word.append(letter)
                        if penalties == 12:
                            txt.lose_text(screen, word)
                            pygame.display.update()
                            pygame.time.delay(3000)
                            pygame.quit()
                            exit()

                    else:
                        in_word.append(letter)
                        hidden_word = hng.reveal_letter(hidden_word, letter, index)
                        if hidden_word == word:
                            txt.win_text(screen, word)
                            pygame.display.update()
                            pygame.time.delay(3000)
                            pygame.quit()

        pygame.display.update()
