list1 = []
a = 1
def nhapKH (list1):
    ten = input('Nhap ten KH: ')
    gt = input('Nam/Nu: ')
    kh = {'ten': ten, 'gt': gt}
    list1.append(kh)
    return

def in_ds (list1):
    for i in list1:
        print (i['ten'], '------', i['gt'])
    return

def tim_kiem (list1):
    x = input('Nhap ten can tim: ')
    count = 0
    for i in list1:
        if i['ten'].lower() == x.lower():
            print (i['ten'], '------', i['gt'])
            count = 1
    if count == 0:
        print ('Khong tim thay gia tri')
    return

def cap_nhat(list1):
    ten = input('Nhap ten KH can cap nhat')
    count = 0
    for i in list1:
        if i['ten'].lower() == ten.lower():
            ten_moi = input('Nhap ten moi can cap nhat: ')
            i['ten'] = ten_moi
            gt_moi = input('Cap nhat lai gioi tinh: ')
            i['gt']= gt_moi
            count = 1
            break
    if count == 0:
        print ('Cap nhat khong thanh cong')
    return

while a == 1:
    print ('1: Them KH | 2: Tim kim | 3: Cap nhat | 4: In')
    a = int(input())
    if a == 1:
        nhapKH(list1)
    elif a == 2:
        tim_kiem(list1)
    elif a == 3:
        cap_nhat(list1)
    elif a == 4:
        print(list1)
    a = int(input('1: Tiep tuc | 2: Dung'))





