from M_so import *

num_list = []
choice = 1
while choice == 1:
    print("1. Nhap vao 1 day so nguyen \n 2. In day so nguyen \n 3. In danh sach cac so nguyen to trong day so da nhap \n 4. In danh sach cac so nguyen chan \n 5. In dach sach cac so nguyen le \n 6. Tong cac so nguyen \n 7. Tong cac so nguyen to\n 8. Tong cac so nguyen chan")
    choice = int(input("Ban muon lam gi ?"))
    if choice == 1:
        input_list(num_list)
    elif choice == 2:
        print(print_list(num_list))
    elif choice == 3:
        print(print_prime(num_list))
    elif choice == 4:
        print(even_num(num_list))
    elif choice == 5:
        print(odd_num(num_list))
    elif choice == 6:
        print(total_list(num_list))
    elif choice == 7:
        print(total_prime_num(num_list))
    elif choice == 8:
        print(odd_prime_total(num_list))
    choice = int(input(print("Ban co muon tiep tuc ? \n 1. Co \n 2. Khong")))
        