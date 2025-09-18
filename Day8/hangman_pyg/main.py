import pygame
import draw  # dessin du bonhomme
import english_words
import texts as txt  # les affichages du text
import py_hangman as hng  # copie du code du jour 7
import string

# initialisations
pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Hangman")

# regularisation image
image = pygame.image.load("sources/backround.jpg")
image_rect = image.get_rect()

# mot à deviner et sa version caché
word = hng.return_random(english_words.get_english_words_set(["web2"], lower=True))
hidden_word = hng.hidden(word)

# compteur des faux essaies
penalties = 0

# compteur pour dessiner le bonhomme
entry_draw = 0

# lettres déjà deviné
not_in_word = []
in_word = []

# parametre de bool pour rentrer dans le jeu
click = False

while True:
    screen.blit(image, image_rect)
    txt.opening_screen(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit

        # verif action pour rentrer dans le jeu
        if event.type == pygame.MOUSEBUTTONDOWN:
            click = True

        if click == True:

            # initialisation de l'écran
            screen.blit(image, image_rect)

            # affichage des textes du debut
            txt.initial_message(screen)
            txt.show_hidden_word(screen, hidden_word)
            txt.show_penalties(screen, penalties)
            txt.guessed_letters(screen, not_in_word, (300, 500))

            # on a uniquement le cas ou on rentre lettre par lettre
            if event.type == pygame.KEYDOWN:

                # on recupere le lettre
                letter = pygame.key.name(event.key)

                # on verifie que la lettre n'était pas déjà mis
                if letter in not_in_word or letter in in_word:
                    txt.repetition_error(screen)
                    pygame.display.update()
                    pygame.time.delay(1000)

                # on verifie que l'input est une lettre
                if letter not in string.ascii_letters:
                    """je ne sais pas comment reussir a garder le message sans le delay"""
                    txt.letter_error(screen)
                    pygame.display.update()
                    pygame.time.delay(1000)

                else:
                    """pourquoi on rentre dans cet else quand inp a déjà sorti ---> je sais parce que penalties augmente"""

                    # lettre est dedans -> renvoiles indices du lettre // lettre n'est pas dedans -> renvoi faux
                    # on note le resultat dans index
                    index = hng.find_letter(word, letter)

                    # cas ou on n'a pas trouvé le lettre
                    if index == False:
                        penalties += 1
                        not_in_word.append(letter)

                        # condition pour gagner
                        if penalties > 12:
                            txt.lose_text(screen, word)
                            pygame.display.update()
                            pygame.time.delay(3000)
                            pygame.quit()

                    # cas ou le lettre est bon
                    else:
                        in_word.append(letter)

                        # on modifie notre mot caché pour qu'elle affiche la lettre trouvé
                        hidden_word = hng.reveal_letter(hidden_word, letter, index)

                        # condition pour gagner
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
