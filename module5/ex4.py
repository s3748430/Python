num_list = [1,2,3,4,5,6,7,8]

total_even_num = 0

for num in num_list:
    if num % 2 != 0:
        continue
    total_even_num += num

print(total_even_num)