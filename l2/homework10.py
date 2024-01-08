import string
import keyword

name = input('Enter a string: ')


if name[0].isdigit():
    print(False)
elif name.isdigit():
    print(False)
elif name in keyword.kwlist:
    print(False)
elif ' ' in name:
    print(False)
elif any(n.isupper() for n in name):
    print(False)
else:
    for n in name:
        if n in string.punctuation and n != '_':
            print(False)
            break
    else:
        print(True)