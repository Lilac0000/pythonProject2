lst = [6]
a = 0

for i in range(0, len(lst), 2):
     a += lst[i]

print(a*lst[-1])
