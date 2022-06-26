"""5kyu: Rot13"""
# ROT13 is a simple letter substituion cipher that replaces a letter with the letter 13
# letters after it in the alphabet. ROT13 is an example of the Caesar cipher.

# Create a function that takes a string and returns the string ciphered with Rot13. If
# there are numbers or special characters included in the string, they should be
# as they are. Only letter from the latin/english alphabet should be shifted, like
# in the original Rot13 "implementation".

import re
import string


def replace(object):
    lower = string.ascii_lowercase * 2
    upper = string.ascii_uppercase * 2

    letter = object.group()
    if letter.islower():
        return lower[lower.index(letter) + 13]
    else:
        return upper[upper.index(letter) + 13]


def rot13(message):
    return re.sub(r"[a-zA-Z]", replace, message)


print(rot13("test2"))  # grfg2
