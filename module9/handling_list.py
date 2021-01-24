from functools import reduce
from operator import add
import lib_handling_prime_num as prime_num

def sum_list(num_list):
    total = reduce(add, list_number)
    return total

def input_list(num_list):
    num = '-1'
    print("Enter a list of number:")
    while num!= '':
        num = input()
        if num != '':
            if prime_num.check_num(num):
                num_list.append(eval(num))
    return
    