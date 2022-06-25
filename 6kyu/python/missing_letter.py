"""6kyu: Find the missing letter"""
# Find the missing letter
# Write a method that takes an array of consecutive (increasing) letters as
# input and that returns the missing letter in the array.

# You will always get an valid array. And it will be always exactly one
# letter be missing. The length of the array will always be at least 2.
# The array will always contain letters in only one case.

import string
def find_missing_letter(chars):

    if ''.join(chars).islower():
        alphabet = list(string.ascii_lowercase)
    else:
        alphabet = list(string.ascii_uppercase)

    first_char_index = alphabet.index(chars[0])

    for letter in alphabet[first_char_index:]:
        if letter not in chars:
            return letter
    