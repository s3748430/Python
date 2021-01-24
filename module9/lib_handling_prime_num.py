def check_num(num_str):
    char ='-'
    if num_str.find(char) == 0:
        num_str = num_str[1:]
        return num_str.isdigit()
    return num_str.isdigit()

def prime_num(num):
    if num <= 1:
        return False
    else:
        for i in range (2, num):
            if num % i == 0:
                return False
        return True
