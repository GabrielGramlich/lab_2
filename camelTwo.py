# This was to attempt to convert camel.py into a list comprehension, but nope. I'll work on this later.

words = input('Please input a sentence: ').split()
first_word = words[0].lower()
camel_case = first_word

rest_of_words = words[1:]
rest_of_words_capitalized = [word[0:1].upper() + word[1:len(word)].lower() for word in rest_of_words]

for word in rest_of_words_capitalized:
    camel_case += word

camel_case = camel_case.replace('.', '')
camel_case = camel_case.replace('#', '')
camel_case = camel_case.replace('/', '')
camel_case = camel_case.replace('\\', '')

print('This is your sentence as a filename in camel case:')
print(camel_case)
