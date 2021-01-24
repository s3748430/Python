def input_cilent(client_list):
    name = input("Enter a name:")
        if name != '':
            phone_number = input(print("Enter phone number:"))
            gender = input(print("Enter gender:"))
            client_list_dic = {'name':name, 'phone_number':phone_number, 'gender':gender}
            client_list.append(cilent_list_dic)

def print_cilent(client_list):
    for ele in client_list:
        print(ele['name'], "-----------", ele['phone_number'], "----------",ele['gender'])

def search_cilent(client_list):
    name = input(print("Enter a name:"))
    count = 0
    for ele in client_list:
        if ele['name'].lower() == name.lower():
            count += 1
            print(ele['name'], "----------", ele['phone_number'], "----------", ele['gender'])
    if count == 0:
        print("Invalid entry")

def update_cilent(client_list):
    client_list[input("key:")] = input("value:")
        