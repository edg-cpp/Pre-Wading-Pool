## Task 3
# 1
"""print("Bonjour, c'est quoi votre surnom?")
stock = input()
print("Bonjour",stock)
"""
# 2
""" print("put a number")
number=input()
print(type(number))
 """

# 3 (premier version)
""" print("put a number")
number1=input()
print("put a number")
number2=input()
n=int(number1)+int(number2)
print (f"The sum of the provided numbers is {n}.")
 """


# 4
def letter_catcher():
    print("write a sentence please")
    sentence = input()
    a = sentence[
        0
    ]  # c'est pas forcement propre parce qu'on suppose que notre phrase commence par un mot
    for i in range(len(sentence) - 2):
        if sentence[i] == " ":
            a += sentence[i + 1]
    print(a)


# letter_catcher()

####Challenge (normalement il y a count)


def word_counter(sentence):
    s_uniform = sentence.lower()
    s_uniform_inv = s_uniform[::-1]
    count = 0
    indice = 0
    words = ["cat", "mice", "garden"]

    # on cherche les mots d'abord normalement
    for w in words:
        while s_uniform[indice:].find(w) != -1:
            indice += s_uniform[indice:].find(w) + len(w)
            count += 1
    indice = 0  # reinitialisation de l'indice

    # on cherche au phrase à l'envers. J'ai pas cherché au sens inverse parce que sinon mon premier indice allait etre -1
    for w in words:
        while s_uniform_inv[indice:].find(w) != -1:
            indice += s_uniform_inv[indice:].find(w) + len(w)
            count += 1
    print(f"count = {count} \nEND")
    return 0


ex1 = "the CataCat attaCk a Cat"
ex2 = "thE Cat's tactic wAS tO surpRISE thE mIce iN tHE gArdeN"

# word_counter(ex1)
# word_counter(ex2)

##3.5 --> doc dedié
