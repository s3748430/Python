try: 
    num_list = []

    while True:
        num_list.append(int(input("Please input your number:")))

except:
    print(num_list)
prime_num_list = []
ele = 0
for ele in num_list:
    for i in range (2, ele):
        if ele % i == 0:
            num_list.remove(ele)
    prime_num_list.append(ele)

print(prime_num_list)



