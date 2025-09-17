# 3.1
student = {"player": "NOM Prénom", "team": "Ekip"}

# 3.2
superhero = {
    " Batman ": {
        "id": 1,
        " aliases ": [" Bruce Wayne ", " Dark knight "],
        " location ": {
            " number ": 1007,
            " street ": " Mountain Drive ",
            " city ": " Gotham ",
        },
    },
    " Superman ": {
        "id": 2,
        " aliases ": ["Kal -El", " Clark Kent ", "The Man of Steel "],
        " location ": {
            " number ": 344,
            " street ": " Clinton Street ",
            " apartment ": "3D",
            " city ": " Metropolis ",
        },
    },
}
# print(superhero[" Superman "][" location "][" city "])

# 3.3
superhero[" Batman "][" aliases "].append("Caped Crusader")
# print(superhero[" Batman "][" aliases "])

# 3.4

dct = {
    " dalmatians ": 101,
    "pi": 3.14,
    " beast ": 3 * 2 * 111,
    " life ": 42,
    " googol ": 10 ^ 100,
}


def max_val(d):
    values = []
    for e in d:
        values.append(d.get(e))
    return max(values)


# print(max_val(dct))

# challenge
import time
import random


def max_of(lst):
    max = lst[0]
    for e in lst:
        if e >= max:
            max = e
    return max


def sort2(lst):
    sorted = []
    for i in range(len(lst)):
        sorted.append(max_of(lst))
        lst.remove(max_of(lst))
    return sorted


l = []
for i in range(10):
    l.append(random.randint(0, 654325613210546456565464))
l2 = l
start = time.time()
sort2(l)
# print(time.time() - start)
