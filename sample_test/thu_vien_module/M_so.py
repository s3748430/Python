def input_list(num_list):
    num = '-1'
    print("Enter a number:")
    while num != '':
        num = input()
        if num != '':
            num_list.append(int(num))

def print_list(num_list):
    return num_list

def prime_num(num):
    if num <= 1:
        return False
    else:
        for i in range (2, num):
            if num % i == 0:
                return False
        return True

def print_prime(num_list):
    for i in num_list:
        if prime_num(i):
            print(i)
    return


def even_num(num_list):
    even_num_list = []
    for i in range (0, len(num_list)):
        if i % 2 == 0:
            even_num_list.append(i)
        i += 1
    return even_num_list

def odd_num(num_list):
    odd_num_list = []
    for i in range (0, len(num_list)):
        if i % 2 != 0:
            odd_num_list.append(i)
        i += 1
    return odd_num_list

def total_list(num_list):
    total = 0
    total = sum(num_list)
    return total

def total_prime_num(num_list):
    total = 0
    for i in num_list:
        if prime_num(i):
            total += i
    return total

def total_even_num(num_list):
    total = 0
    for i in num_list:
        if i % 2 == 0:
            total += i
    return total
    










