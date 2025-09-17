# 2.2


def exo(word):
    result = ""
    for e in word:
        result += e * 2
    print(result)


word = "taxi"
# exo(word)

# 2.3
import math


def div7(nb):
    for i in range(nb, 1, -1):  # il fallait mettre le plus grand nb en premier
        if i % 7 == 0:
            print(i)


# div7(10000)


def fizzbuzz():
    for i in range(-30, 31):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)


# fizzbuzz()


# 2.5
def NNBottlesOfBeer():
    for n in range(99, 2, -1):
        print(
            f"{n} bottles of beer on the wall.\n{n} bottles of beer.\nIf one of the bottles just happen to fall,\n{n-1} bottles of beer on the wall. \n"
        )
        print(
            "2 bottles of beer on the wall.\n2 bottles of beer.\nIf one of the bottles just happen to fall,\nOne bottle of beer on the wall. \n"
        )
        print(
            "One bottle of beer on the wall.\nOne bottle of beer.\nIf one of the bottles just happen to fall,\nNo more bottles of beer on the wall. \n"
        )
        print(
            "No more bottles of beer on the wall,\nno more bottles of beer.\nGo to the store and buy some more,\n99 bottles of beer on the wall... "
        )


# NNBottlesOfBeer()


# 2.6
def div_list(nb):
    for n in range(2, int(nb / 2) + 1):
        for i in range(nb - 1, 1, -1):
            if i % n == 0:
                print(i, end=" ")
        print(" ")


# div_list(14)


# challenge ------------------------->malfait
def challenge(entry):
    string = entry
    integer = entry
    vowels = ["a", "e", "i", "o", "u"]
    string_cond = filter(
        lambda letter: letter in vowels, string
    )  # find / find all peut fonctionner aussi
    print(string_cond)
    if integer == 0:
        print("no:(")
    if integer >= 42:
        print(integer)
    else:
        print(string)

    # filter --> tri une ensemble avec une fonction
    # lambda permet d'écrire une fonciton dans une maniere anonyme et "sur place"
    # filter retourne pas vrai ou false ça recrée une list --> à voir apres


# challenge()
