number = 0 
total = 0
print("Please input your number:")
while number != '':
    number = input()
    if number != '':
        total += int(number)
print(total)