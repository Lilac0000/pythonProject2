import string
user_input = input("Enter 2 letters with with - : ")
a = string.ascii_letters


first_letter, second_letter = user_input.split('-')
first_index = a.index(first_letter)
second_index = a.index(second_letter)
result = a[first_index:second_index + 1]


print("Result:", result)