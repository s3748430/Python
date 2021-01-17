phone_book = []

choice = 1
while choice ==1:
    print("1. Show phone book | 2. Search phone book | 3. Add new entry")
    choice = int(input("What do you want to do ?"))
    if choice == 1:
        for ele in phone_book:
            print(ele['name'], "-----------", ele['phone_number'])
    elif choice == 2:
        name = input(print("Enter a name:"))
        count = 0
        for ele in phone_book:
            if ele['name'].lower() == name.lower():
                count += 1
                print(ele['name'], "----------", ele['phone_number'])
        if count == 0:
            print("Invalid entry")
    elif choice == 3:
        name = input("Enter a name:")
        if name != '':
            phone_number = input(print("Enter phone number:"))
            phone_book_dic = {'name':name, 'phone_number':phone_number}
            phone_book.append(phone_book_dic)
    choice = int(input(print("Do you want to continue ? (1. Yes | 2. No):")))