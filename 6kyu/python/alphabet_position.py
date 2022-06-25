"""6kyu: Replace With Alphabet Position"""
# In this kata you are required to, given a string, replace every letter with its
# position in the alphabet.

# If anything in the text isn't a letter, ignore it and don't return it

import re
import string

def replace(match_object):
    try: 
        letter = match_object.group()
        return f"{string.ascii_lowercase.index(letter) + 1} "
    except ValueError:
        return ""

def alphabet_position(text):
    return re.sub(r"(.)", replace, text.lower())[:-1]

print(alphabet_position("The sunset sets at twelve o' clock."))