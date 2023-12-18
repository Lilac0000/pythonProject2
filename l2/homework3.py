x = input('Enter a 5 digit-number: ')
digit_1 = int(x) // 10000
digit_2 = int(x) % 10000 // 1000
digit_3 = int(x) % 1000 // 100
digit_4 = int(x) % 100 // 10
digit_5 = int(x) % 10
print(digit_5)
print(digit_4)
print(digit_3)
print(digit_2)
print(digit_1)