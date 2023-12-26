input_list = [1, 2, 3, 4, 5]
middle = len(input_list) // 2


first_list = input_list[:middle]
second_list = input_list[middle:]

if len(input_list) % 2 != 0:
    first_list.append(second_list.pop(0))

elif not input_list:
    first_list = []
    second_list = []

print(first_list, second_list)


















