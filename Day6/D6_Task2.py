####1
def sum_rec(n):
    if n < 0 or type(n) != int:
        print("must be positive and an integer")
        return False

    elif n == 0:
        return 0
    else:
        stock = n + sum_rec(n - 1)
        return stock


# print(sum_rec(42))

####2

import string


def palindrome_check(str):
    str_unif = ""
    for e in str:
        if e in string.ascii_letters:
            str_unif += e.lower()

    if len(str_unif) == 0 or len(str_unif) == 1:
        return True

    if str_unif[0] is not string.ascii_letters:
        return palindrome_check(str_unif[1:])

    if str_unif[-1] is not string.ascii_letters:
        return palindrome_check(str_unif[:-1])

    else:
        if str_unif[0].lower() == str_unif[-1].lower():
            return palindrome_check(str_unif[1:-1])
        else:
            return False


# print(palindrome_check("never odd or even"))
# print(palindrome_check("A Santa Lived As a Devil at NASA"))

#### 3
import os

# print([x for x in os.listdir(".")])


def list_direc():
    for root, dirs, files in os.walk("./wading_pool"):
        print(root)
        ls = os.listdir(root)
        for e in ls:
            if e[0] == ".":
                ls.remove(e)
        print([e for e in ls], "\n")

        # j'enleve les archives
        for e in dirs:
            if e[0] == ".":
                print("++++++++++", e)
                dirs.remove(e)  #### ne fonctionne pas, d'ou le manuel

        if "__pycache__" in dirs:
            dirs.remove("__pycache__")  # don't visit __pycache__ directories
        if ".archive" in dirs:
            dirs.remove(".archive")  # don't visit __pycache__ directories
        if ".venv" in dirs:
            dirs.remove(".venv")  # don't visit __pycache__ directories
        if ".git" in dirs:
            dirs.remove(".git")  # don't visit __pycache__ directories
        if ".vscode" in dirs:
            dirs.remove(".vscode")  # don't visit __pycache__ directories


list_direc()

# comment acceder directement au contenu
# comment faire en sorte de ne pas rentrer dans ces choses sans les definir à la main?
