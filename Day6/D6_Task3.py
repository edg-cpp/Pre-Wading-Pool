#### 1 version rec !!!!!!!!!!!!!!!!!!!!!!!! ça fonctionne pas mais c'est abandonné
import string


def funA_rec(s, n):
    count = 0
    if s == "":
        return False  # pas possible
    else:
        if n - count == 0:
            return True
        else:
            count += 1
            return funA_rec(s[1:], n)


def funB_rec(s, n):
    count = 0
    if s == "":
        return False
    else:
        if n - count == 0:
            return True
        else:
            if s[0] in string.punctuation:
                count += 1
            return funB_rec(s[1:], n)


def funC_rec(s, n):
    count = 0
    if s == "":
        return False
    else:
        if n - count == 0:
            return True
        else:
            if s[0] in string.digits:
                count += 1
            return funB_rec(s[1:], n)


# print(funA_rec("ceciEstUnm0tdePa$$e", 5))
# print(funB_rec("ceciEstUnm0tdePa$$e", 1))
# print(funC_rec("ceciEstUnm0tdePa$$e", 1))


#### 1 version normal
def funA(n, s):
    return len(s) >= n


def funB(n, s):
    count = 0
    for e in s:
        if e in string.punctuation:
            count += 1
    return count >= n


def funC(n, s):
    count = 0
    for e in s:
        if e in string.digits:
            count += 1
    return count >= n


""" 
print(funA(10, "ceciEstUnm0tdePa$$e"))
print(funB(1, "ceciEstUnm0tdePa$$e"))
print(funC(1, "ceciEstUnm0tdePa$$e"))
"""

#####2


def passcheck(func, n, s):
    return func(n, s)


passcheck(funA, 16, " mysecretpassword ")
passcheck(funB, 3, " mysecretpassword ")
passcheck(funC, 1, " mysecretpassword ")


####3
def passcheck_2(func, n, s):
    if n is not int:
        print("the limit must be an integer")
        return 0

    elif func(n, s) is not bool:
        print("the function must return bool")
        return 0

    elif s is not string:
        print("Your password must be a string")
        return 0
    else:
        return func(n, s)
