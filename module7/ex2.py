lst = []
number = 0
print("Enter your number:")
while number != '':
    number = input()
    if number.isdigit():
            lst.append(eval(number))

n = eval(input(print("Enter the number you wanna find:")))

print("Your list :", lst)

if n in lst:
    print("Your number %d appear %d time in list"%(n, lst.count(n)))
else:
    print("Your number %d does not appear in list"%n)

max_num = max(lst)
if n > max_num:
    print("%d is largest digit"%n)
else:
    lst_1 = []
    for item in lst:
        if item > n:
            lst_1.append(item)
    print("The number larger than %d is"%n, lst_1)
