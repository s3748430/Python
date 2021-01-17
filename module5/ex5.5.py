n = int(input("Enter a number:"))

Sum_a = Sum_b = Sum_d = 0
Sum_c = 1
A_str = B_str = C_str = D_str =''

for i in range (1, n+1):
    if i % 2 != 0:
        Sum_a += i
        A_str += str(i) +'+'
    
    if i % 2 == 0:
        Sum_b += i
        B_str += str(i) +'+'
    
    Sum_c *= i
    C_str += str(i) + '*'

    if i > 1:
        flag = True
        for j in range (2, i):
            if i % j == 0:
                flag = False
                break
        if flag == True:
            Sum_d += i
            D_str += str(i) + '+'

print('A = %s = %d'%(A_str, Sum_a))
print('B = %s = %d'%(B_str, Sum_b))
print('C = %s = %d'%(C_str, Sum_c))
print('D = %s = %d'%(D_str, Sum_d))
    