# 2.2
# print([x + 10 for x in [3, 2, 6, 7, 1, 4]])
# boucle for dans le list pour faire un ajout

# 2.3
a = list(filter(lambda x: x > 10, [42, 3, 4, 7]))
# print(a)
# lambda --> fonction indirect // filter --> applique le fonction au liste // list --> fait en sorte aue la nouvelle liste filtré soit bien une list et non une adresse


# 2.4 (sans utiliser min et max du coup)
def min_max(list):
    min = list[0]
    max = list[0]
    for e in list:
        if e >= min:
            min = e
        if e >= max:
            max = e
    return min, max


# 2.5
lst = [1, 6, 2, 5, 54, 3]
# lst.sort(reverse=True)  # ça modifie la liste déjà là
# print(lst)


# 2.5.2
def sorting(lst):
    sorted = []
    for i in range(len(lst)):
        sorted.append(max(lst))
        lst.remove(max(lst))
    return sorted


# print(sorting(lst))

# 2.6
"""pour tout les x appertenant au list donné, divise les x en deux s'ils sont paires. Sinon multiplie les en deux"""
# print([x // 2 if x % 2 == 0 else x * 2 for x in [42, 3, 4, 18, 3, 10]])

# 2.7
# print([*enumerate([42, 3, 4, 18, 3, 10])])
# omg ça renvoi la meme liste avec ses indices <3
# sans étoile : [<enumerate object at 0x7f77f1d6ba10>]
#### * c'est utilisé pour acceder au contenu

# 2.8
first_names = [" Jackie ", " Chuck ", " Arnold ", " Sylvester "]
last_names = [" Stallone ", " Schwarzenegger ", " Norris ", " Chan "]
magic = [*zip(first_names, last_names[::-1])]
""" print(magic[0])
print(magic[3])
print(magic[1][0])
print(magic[0][1])
print(magic[2])
 """
# omg zip met ensemble les deux listes dans l'ordre que tu veux (dans notre cas la deuxieme est à l'envers)
