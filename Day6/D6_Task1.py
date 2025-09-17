##### 1
"""
42
52
"""


##### 2
def bread():
    print(" <////////// > ")


def lettuce():
    print(" ~~~~~~~~~~~~ ")


def tomato():
    print(" O O O O O O ")


def ham():
    print(" ============ ")


def sandwich():
    bread()
    lettuce()
    tomato()
    ham()
    ham()
    bread()


##### 3
""" 
for i in range(4):
    sandwich()
"""


####4
def sandwich_maker(n):
    if n > 0 and type(n) == int:
        for i in range(n):
            sandwich()
    else:
        print("I can't do this!")


""" 
sandwich_maker(1)
sandwich_maker(-8)
sandwich_maker(3.2)
"""

#### 4


#### challenge
def ch1(number, power):
    s = 1
    for i in range(power):
        s *= number
    return s


def ch2(number, power):
    if power == 0:
        return 1
    return number * ch2(number, power - 1)


import time

start1 = time.time()
ch1(42, 168)
print(f"Time taken with ch1 for 42^168: {time.time() - start1}")

start2 = time.time()
ch2(42, 168)
print(f"Time taken with ch2 for 42^168: {time.time() - start2}")

start1 = time.time()
ch1(42, 84)
print(f"Time taken with ch1 for 42^82: {time.time() - start1}")

start2 = time.time()
ch2(42, 84)
print(f"Time taken with ch2 for 42^82: {time.time() - start2}")
