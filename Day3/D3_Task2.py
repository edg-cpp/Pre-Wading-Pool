##Task 2
# 1
a = "TEXT"
a = a.lower()
# print(a)

# 2
b = "tutu on the tuki-kata"
b = b.replace("tu", "ta")
# print(b)

# 3
# prediction: ça va dire not found?
string = " Hello world !"
position = string.find("a")
# print ( position )

# If the value is not found, the find() method returns -1 (askip)

# 4
# prediction: ij abcdef j cdefghij  mais sans les espaces
p = "abcdefghij"
# print (p[:: -2][:5][:: -1][3:])

# chokbar
# https://zestedesavoir.com/tutoriels/582/les-slices-en-python/
# enfait le bidule c'est pas :: mais c'est plutot [a:b:c] avec a pour le debut b pour le fin et c pour le direction(+/-) et l'écart de saut
# c'est juste qu'on a le droit de laisser vide
# et en haut ça excecute dans l'ordre comme des trucs séparé

# 5
"""
ça regarde la partie entre () pour faire l'operation
(p)[:: -2] = igeca
(p[:: -2])[:5] = igcea
(p[:: -2][:5])[:: -1] = aecgi
(p[:: -2][:5][:: -1])[3:] = i
"""

# 6
# print(a*10)

# 7
# print("hello"+ 42) ==> can only concatenate str (not "int") to str
# print("hello"+ "42")

# 8
s1, s2, s3 = "42", "is", "the answer"
# print ("\"",s1,s2,s3,"\"", "contains", len(s1+s2+s3),"charachters.") #il doit y avoir une maniere plus jolie de faire ça
