my_list = input("Enter the number with space -"). split()
for i in range(0, len(my_list), 2):
    my_list[i + 1], my_list[i] = my_list[i], my_list[i + i]

print(my_list)

