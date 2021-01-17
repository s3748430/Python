import math

a = eval(input("Enter a:"))
b = eval(input("Enter b:"))
c = eval(input("Enter c:"))

if a == 0:
    if b ==0 and c != 0:
        print("Phương trình vô nghiệm")
    elif b == 0 and c == 0 :
        print("Phương trình vô số nghiệm")
    else:
        print("Nghiệm của phương trình x = %0.2f"%(-c/b))

else:
    delta = pow(b,2)-4*a*c
    if delta < 0:
        print("Phương trình vô nghiệm")
    elif delta == 0:
        print("Phương trình có nghiệm kép x1 = x2 = %0.2f"%((-b/(2*a)))
    else:
        x1 = -(b - math.sqrt(delta))/(2*a)
        x2 = -(b + math.sqrt(delta)) / (2*a)
        print("Phương trình có 2 nghiệm phân biệt")
        print("x1 = %0.2f"%x1)  
        print("x2 = %0.2f"%x2)      