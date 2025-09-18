import pygame
import draw  # dessin du bonhomme
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


# font=pygame.font.SysFont()
click = False

while True:
    screen.blit(image, image_rect)
    txt.opening_screen(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit

        if event.type == pygame.MOUSEBUTTONDOWN:
            click = True

        if click == True:
            screen.blit(image, image_rect)
            txt.initial_message(screen)
            txt.show_hidden_word(screen, hidden_word)
            txt.show_penalties(screen, penalties)
            txt.guessed_letters(screen, not_in_word, (300, 500))

            if event.type == pygame.KEYDOWN:
                inp = pygame.key.name(event.key)
                inp = inp.lower()

                if inp in not_in_word or inp in in_word:
                    txt.repetition_error(screen)
                    pygame.display.update()
                    pygame.time.delay(1000)

                if inp not in string.ascii_letters:
                    txt.letter_error(screen)
                    pygame.display.update()
                    pygame.time.delay(1000)

                else:
                    letter = inp
                    index = hng.find_letter(word, letter)
                    if index == False:
                        penalties += 1
                        not_in_word.append(letter)
                        if penalties > 12:
                            txt.lose_text(screen, word)
                            pygame.display.update()
                            pygame.time.delay(3000)
                            pygame.quit()

                    else:
                        in_word.append(letter)
                        hidden_word = hng.reveal_letter(hidden_word, letter, index)
                        if hidden_word == word:
                            txt.win_text(screen, word)
                            pygame.display.update()
                            pygame.time.delay(3000)
                            pygame.quit()

        # for event in pygame.event.get():
        #    if event.type == pygame.QUIT:
        #        pygame.quit()
        #        raise SystemExit

        #    txt.print_check(screen, "Click to try again")
        #    pygame.time.delay(3000)

        #    if event.type == pygame.MOUSEBUTTONDOWN:
        #        word = hng.return_random(
        #            english_words.get_english_words_set(["web2"], lower=True)
        #        )
        #        hidden_word = hng.hidden(word)
        #        penalties = 0
        #        not_in_word = []
        #        in_word = []
        #        click = True

        pygame.display.update()
