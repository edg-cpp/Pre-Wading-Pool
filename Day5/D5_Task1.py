# 1.1

my_first_list = [4, 5, 6]
my_second_list = [1, 2, 3]
my_first_list.extend(my_second_list)
"""prediction: on va avoir un list qui va donner [4,5,6,1,2,3]"""
# print(my_first_list)

my_first_list = [7, 8, 9]
my_second_list = [4, 5, 6]  # ça fait la meme travail qu'avant
my_first_list = [*my_first_list, *my_second_list]  # ça fait la meme travail qu'avant
etoile_imp = [my_first_list, my_second_list]
# crée un list a deux elements avec les elts etant les deux
#  donnés

# print(my_first_list)
