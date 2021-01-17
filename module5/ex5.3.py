n = int(input("Enter number n:"))

x = int(input("Enter number x:"))

total_1 = (x ** 2 + x + 1)
total_2 = (x ** 2 - x + 1)

print(total_1)
print(total_2)

while n > 0:
    total_1 *= total_1
    n -= 1

while n > 0:
    total_2 *= total_2
    n -= 1

total = total_2 + total_1
print(total)

