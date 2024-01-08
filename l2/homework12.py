import string

hashtag = input('Enter a string: ')

for symbol in string.punctuation:
    hashtag = hashtag.replace(symbol, "")

hashtag = hashtag.title()
hashtag = "#" + hashtag
hashtag = hashtag[:140]

print(hashtag)
