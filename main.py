import string
import random


def get_uppercase_array():
    alphabet_uppercase = string.ascii_uppercase
    uppercase_array = []
    for x in alphabet_uppercase:
        uppercase_array.append(x)
    return uppercase_array


def get_lowercase_array():
    alphabet_lowercase = string.ascii_lowercase
    lowercase_array = []
    for x in alphabet_lowercase:
        lowercase_array.append(x)
    return lowercase_array


def is_uppercase(letter):
    return letter in get_uppercase_array()


def is_lowercase(letter):
    return letter in get_lowercase_array()


def encode_text(content: str):
    transformed_text = ''
    random_int = random.randint(0, len(get_lowercase_array()) - 1)
    word_split = get_lowercase_array()[random_int - 1]
    word_split += word_split
    for x in content:
        if is_uppercase(x):
            to_append = ''
            for y in range(0, get_uppercase_array().index(x) + 1):
                to_append += get_uppercase_array()[random_int]
            transformed_text += to_append + word_split
        elif is_lowercase(x):
            to_append = ''
            for y in range(0, get_lowercase_array().index(x) + 1):
                to_append += get_lowercase_array()[random_int]
            transformed_text += to_append + word_split
        else:
            transformed_text += str(x)
    return transformed_text


def decode_text(content: str):
    untransformed_text = ''
    word_split = get_lowercase_array()[get_lowercase_array().index(content[0].lower()) - 1]
    word_split += word_split
    words = content.split(' ')
    for x in words:
        letters_array = x.split(word_split)
        letters_array.pop(len(letters_array) - 1)
        word = ''
        for y in letters_array:
            if y.isupper():
                index = len(y) - 1
                letter = get_uppercase_array()[index]
                word += letter
            elif y.islower():
                index = len(y) - 1
                letter = get_lowercase_array()[index]
                word += letter
        untransformed_text += word + ' '
    return untransformed_text


def main_loop():
    print('1. Encode')
    print('2. Decode')
    chosen = int(input('Choose a function: '))

    if chosen == 1:
        text = input('Enter your text: ')
        print(f'Output: {encode_text(text)}')
    elif chosen == 2:
        text = input('Enter your text: ')
        print(f'Output: {decode_text(text)}')
    else:
        print('INCORRECT FUNCTION!')
        main_loop()


if __name__ == '__main__':
    main_loop()
