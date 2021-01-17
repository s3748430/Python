tup1 = ("tiger", "cat", "dog","mouse","rabbit", "chicken", "tiger", "tiger", "mouse")

positiv_num = int(input("Input a number (0-9)"))
negativ_num = int(input("Input a number (-1 -> -9)"))
find = input(print("Enter a word to find:"))

print("Tuple[%d]"%positiv_num, tup1[positiv_num])
print("Tuple[%d]"%negativ_num, tup1[negativ_num])
print("%s appear in the tuple %d"%(find, tup1.count(find)))