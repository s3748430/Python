number = int(input("Enter a number:"))

flag = True
for i in range (2, number):
    if number % i == 0:
        flag = False
        break

if flag == True:
    print(number, "is a prime number")
else:
    print(number, "is not a prime number")