# 4.1
def invitation_check(name, lst):
    if name in lst:
        print("Welcome in !")
        return True
    else:
        print("Get lost!!!")
        return False


lst = ["Name 1", "Name 2", "Name Surname", "Surname Name"]
# invitation_check("Name 1", lst)
# invitation_check("Name", lst)

# 4.2


######################## trop de loop --> à optimiser
def erase_dup(lst):
    indices = []
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            if i != j and (i or j not in indices) and lst[i] == lst[j]:
                indices += [j]
    return [lst.pop(i) for i in indices]


print(erase_dup([1, 1, 2, 2, 3]))
