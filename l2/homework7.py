lst = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]


for el in lst[:]:
    if el == 0:
        lst.append(lst.pop(lst.index(0)))

print(lst)



