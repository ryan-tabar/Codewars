"""7kyu: Vowel Count"""

# Return the number (count) of vowels in the given string.

import re

def getCount(inputStr):
    return len(re.findall(r"[aeiou]", inputStr))

print(getCount("Should count all vowels"))