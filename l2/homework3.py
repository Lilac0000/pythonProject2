x = input('Enter a 5 digit-number: ')
digit_1 = int(x) // 10000
digit_2 = int(x) % 10000 // 1000
digit_3 = int(x) % 1000 // 100
digit_4 = int(x) % 100 // 10
digit_5 = int(x) % 10
digit_6 = digit_5 * 10000 + digit_4 * 1000 + digit_3 * 100 + digit_2 * 10 + digit_1 * 1
print(digit_6)


