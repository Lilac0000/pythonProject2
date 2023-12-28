lst = []
a = 0

for i in range(0, len(lst), 2):
     a += lst[i] if i < len(lst) else 0

print(a*lst[-1] if lst else 0)
