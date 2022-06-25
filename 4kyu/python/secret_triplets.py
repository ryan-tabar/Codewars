"""4kyu: Recover a secret string from random triplets"""
# There is a secret string which is unknown to you. Given a collection of
# random triplets from the string, recover the original string.

# A triplet here defined as a sequence of three letters such that each letter
# occurs somewhere the next in the given string. "whi" is a triplet for the string
# "watisup".

# As a simplification, you may assume that no letter occurs more than once
# in the secret string.

# You can assume nothing about the triplets given to you other than that they are
# valid triplets and that they contain sufficient information to deduce the original strng,
# In particular, this means that the secret string will never contain letters that 
# do not occur in one of the triplets given to you.


def fix(r, letter1, letter2):
    """let r.index(letter1) < r.index(letter2)"""
    if r.index(letter1) > r.index(letter2):
        r.remove(letter1)
        r.insert(r.index(letter2), letter1)


def recoverSecret(triplets):
    r = list(set([i for l in triplets for i in l]))
    for triplet in triplets:
        fix(r, triplet[1], triplet[2])
        fix(r, triplet[0], triplet[1])
    return "".join(r)
