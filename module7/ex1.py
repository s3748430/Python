list_of_animal = ['ant', 'dog', 'cat','lion','tiger']
print("Number of animals:", len(list_of_animal))
find = input("I wanna find:")


if find in list_of_animal:
    print("There is a %s in the list of animal"%find)
else:
    print("There is no %s in the list of animal"%find)