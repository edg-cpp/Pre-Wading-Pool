import pygame
import op_screen as ops

pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Hangman")

image = pygame.image.load("sources/backround.jpg")
image_rect = image.get_rect()


while True:
    screen.blit(image, image_rect)
    ops.opening_screen(screen)

    pygame.event.set_blocked(pygame.MOUSEBUTTONDOWN)
    ev = pygame.event.wait()

    for event in pygame.event.get():
        screen.blit(image, image_rect)
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                user_text = user_text[:-1]
            else:
                user_text += event.unicode
    pygame.display.update()

############################### Le programme


def hangman():
    guess = True
    word = return_random(words_set)
    hidden_word = hidden(word)
    penalties = 0
    not_in_word = []
    in_word = []

    print("HANGMAN\n")
    print(
        "Hello and welcome to the game of Hangman where you'll try to guess a random word.\n"
    )
    print("===CHOOSE DIFFICULTY LEVEL===")
    print("1. Easy : 18 Penalties")
    print("2. Normal : 12 Penalties")
    print("3. Difficult : 9 Penalties")
    print("4. Quit")
    level = input("Put the corresponding number to make yout choice: ")
    match level:
        case "1":
            nb_penalties = 18
            print(
                f"You have {nb_penalties} penalties. If you want to quit the game, enter 'quit' when a letter is asked. \nEnjoy!"
            )

        case "2":
            nb_penalties = 12
            print(
                f"You have {nb_penalties} penalties. If you want to quit the game, enter 'quit' when a letter is asked. \nEnjoy!"
            )

        case "3":
            nb_penalties = 9
            print(
                f"You have {nb_penalties} penalties. If you want to quit the game, enter 'quit' when a letter is asked. \nEnjoy!"
            )
        case "4":
            guess = False

    # la premiere list c'est pour ceux qui ne sont pas dans le mot et la deuxieme c'est pour ceux qui sont dans le mot
    while guess:

        # Le Début
        print(f"{hidden_word} | {penalties} penalties")

        if not_in_word != []:
            print("Letters are not in the word:")
            print(not_in_word)

        letter = input("Please enter a letter: ").lower()

        if letter == "quit":
            guess = False

        # Les Erreurs:
        elif letter in in_word or letter in not_in_word:
            print("You already guessed this letter\n")

        elif letter not in string.ascii_letters:
            print("Error : you must enter a letter\n")

        # Le Jeu
        else:
            index = find_letter(word, letter)
            if index == False:
                penalties += 1
                not_in_word.append(letter)
                print(f"The letter '{letter}' is not in the word")
                if penalties < nb_penalties:
                    print("Try again!\n")
                else:
                    print(f"You've lost :(( The word was: {word}")
                    guess = False
            else:
                in_word.append(letter)
                hidden_word = reveal_letter(hidden_word, letter, index)
                print("Way to go! \n")
                if hidden_word == word:
                    print(f"Congratulations!! The word is {word}. You've WON!!!!")
                    guess = False

    print("Thank you for playing the game!")
