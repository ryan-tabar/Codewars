"""Simple Pig Latin"""
# Move the first letter of each word to the end of it, then add "ay" to the end
# of the word. Leave punctuation marks untouched.

# Examples:
# pig_it("Pig latin is cool") igPay atinlay siay oolcay
# pig_it("Hello world !") # elloHay orldway !

import re

def pig_it(text):
    return re.sub(r"(\w)(\w*)", r"\2\1ay", text)

print(pig_it("Pig latin is cool")) # expect: igPay atinlay siay oolcay