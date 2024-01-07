import string

str_input = input('Enter a string: ')
hashtag = "#" + str_input

hashtag = hashtag[:140]

hashtag = hashtag.title()

hashtag = hashtag.replace(" ", "")
for symbol in string.punctuation:
    if symbol != '#':
        hashtag = hashtag.replace(symbol, "")

print(hashtag)