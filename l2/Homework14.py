number = int(input("Enter a number : "))

result = 1
str_number = str(number)


while number > 9:
    for digit_str in str_number:
        digit = int(digit_str)
        result *= digit

    number = result
    str_number = str(number)
    result = 1

print(f"Result of multypliung : {number}")