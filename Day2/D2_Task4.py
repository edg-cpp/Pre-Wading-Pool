import math

# task 4.1


def convergence_leibniz(a):
    n = 0
    k = 0
    eps = 1
    while abs(eps) > 10 ** (-a - 1):
        n += 4 * (((-1) ** k) / ((2 * k) + 1))
        k += 1
        eps = n - math.pi
    return n, k


# print(convergence_leibniz(6))

# task 4.2


def f(k, lim):
    if lim == 0:
        return 0
    else:
        decrement = lim
        decrement -= 1
        etape = ((2 * k + 1) ** 2) / (6 + f(k + 1, decrement))
        return etape


print(f(0, 2))
print(f(0, 3))


def pi_en_rec(decimale):
    eps = 1
    lim = 0
    fk = 0
    while abs(eps) > 10 ** (-decimale - 1):
        fk = f(0, lim)
        lim += 1
        eps = fk + 3 - math.pi
    return fk + 3, lim


print(pi_en_rec(6))
