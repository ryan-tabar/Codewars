"""7kyu: Credit Card Mask"""
# Usually when you buy something, you're asked whether your credit card number,
# phone number or answer to your most secret qustion is still correct.
# However, since someone could look over your shoulder, you don't want that shown on your screen.
# Instead, we mask it.

# Your task is to write a function maskify, which changes all but the last four characters into "#".

def maskify(string):
    return "#"*(len(string) - 4) + string[-4:]

print(maskify("ab"))