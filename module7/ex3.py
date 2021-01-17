lst = []
prime_lst =[]
number = 0
print("Enter your number:")
while number != '':
    number = input()
    if number.isdigit():
            lst.append(eval(number))

print("Your list is:", lst)

flag = True
for item in lst:
    for i in range (2, item):
        if item % i == 0:
            flag = False
            break
    if flag == True:
        prime_lst.append(prime_lst)

print("Prime number in list :"prime_lst)