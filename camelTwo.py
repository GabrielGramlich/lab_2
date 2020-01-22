# This was to attempt to convert camel.py into a list comprehension, but nope. I'll work on this later.

def main():
    display_banner()
    words = get_input()
    camel_case = perfrom_camel_casing(words)
    camel_case_validated = validate_camel_case(camel_case)
    display_camel_case(camel_case_validated)


def display_banner():
    print('\n')
    message = "* thisIsTheGreatestProgramYouWillEverUse *"
    print('*' * len(message))
    print(message)
    print('*' * len(message))
    print('\n')


def get_input():
    words = input('Please input a sentence: ').split()
    return words


def perfrom_camel_casing(words):
    first_word = words[0].lower()
    camel_case = first_word

    rest_of_words = words[1:]
    rest_of_words_capitalized = [word[0:1].upper() + word[1:len(word)].lower() for word in rest_of_words]

    for word in rest_of_words_capitalized:
        camel_case += word

    return camel_case


def validate_camel_case(camel_case):
    camel_case = camel_case.replace('.', '')
    camel_case = camel_case.replace('#', '')
    camel_case = camel_case.replace('/', '')
    camel_case = camel_case.replace('\\', '')

    return camel_case


def display_camel_case(camel_case):
    print('This is your sentence as a filename in camel case:')
    print(camel_case)


main()
