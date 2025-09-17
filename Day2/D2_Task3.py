# task 3.1
def div_euc(a, b):
    divr = a / b
    divn = a // b
    rem = a % b
    return divr, divn, rem


# print(div_euc(42,4))

# task 3.2


def even(a):
    if a % 2 == 0:
        print("the number is even")
        return 1
    else:
        print("the number is odd")
        return 0


# task 3.3
def sum_dig(a):
    sum = 0
    while a != 0:
        reste = a % 10
        sum += reste
        a -= reste
        a /= 10
    return sum


# print(sum_dig(123434565))
# print(1+2+3+4+3+4+5+6+5)


# task 3.4
def part_int(a):
    return int(a)


# print(int(12.324))


# task 3.5
def part_dec(a):
    stock = a % 1
    return format(stock, "g")


# print(part_dec(12.24))
# print(part_dec(424242.8412))
