############################### Les Imports
import random
from english_words import get_english_words_set  # j'ai la nouvelle version
import string
import os

############################### Les fonctions Intermedieres


def twelve(n):
    if n >= 12:
        print("You lose!")
        return 0


def return_random(st):
    # sets are unordered and unindexed
    x = random.choice(list(st))
    return x


words_set = get_english_words_set(["web2"], lower=True)


def hidden(str):
    a = ["_" for x in str]
    return "".join(
        a
    )  # convertit un liste/tuple en string et mettant ce qui entre gymets entre les elements du array


def find_letter(str, letter):
    if letter in str:
        index = [str.find(letter, i) for i in range(len(str))]
        index = list(set(index))  # on enleve les doublons
        # c'est un if parce que si le lettre est au derniere position on a n'a jamais -1
        if -1 in index:
            index.remove(-1)
        return index
    else:
        return False


def reveal_letter(str, letter, i_list):
    str_l = [s for s in str]
    for i in i_list:
        str_l[i] = letter
    str = "".join(str_l)
    return str


############################### PseudoCode - Le plan des cas
"""
def hangman():
    affiche mot _ _ _ _ comme ça + les penalties
    **entre le lettre
    
    lettre = quit ?
    lettre dans not_in_word?
    lettre dans in_word?
    lettre est bien une lettre ?
    alors jeu:
        lettre pas dans mot ?
            penalties <12?
            sinon 
                ----------> fin de jeu
        lettre dans mot?
            mot trouve ? 
                ----------> fin de jeu
            sinon

"""
############################### Le programme


def hangman():
    os.system("clear")
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


hangman()

######################## Remarques:
"""
find letter + reveal letter à optimiser
"""
