def nhap_so (list1):
    a = '1'
    print ('Nhap danh sach so nguyen, ket thuc bang enter')
    while a!= '':
        a = input()
        if a != '':
            list1.append(int(a))
    print (list1)
    return


def in_so (list1):
    print (list1)
    return

def so_nguyen_to (a):
    if a <=1:
        return False
    else:
        for i in range (2,a):
            if a%i == 0:
                return False
    return True

def in_so_nt (list1):
    list2 = []
    for i in list1:
        if so_nguyen_to(i):
            list2.append(i)
    print (list2)
    return

def in_chan (list1):
    for i in list1:
        if i %2 == 0:
            print (i)
    return

def in_le (list1):
    for i in list1:
        if i%2 == 1:
            print (i)
    return

def tong_ds (list1):
    s = 0
    for i in list1:
        s += i
    return s

def tong_nto (list1):
    s = 0
    for i in list1:
        if so_nguyen_to(i):
            s += i
    return s

def tong_chan (list1):
    s = 0
    for i in list1:
        if i%2 == 0:
            s += i
    return s

def tong_le (list1):
    s = 0
    for i in list1:
        if i%2 == 1:
            s += i
    return s



