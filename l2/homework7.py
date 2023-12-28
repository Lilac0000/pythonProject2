lst = [1, 0, 13, 0, 0, 0, 5]

l = [i for i, num in enumerate(lst) if num == 0]


for i in l[::-1]:
    lst.pop(i)
    lst.append(0)

print(lst)












