"""5kyu: RGB To Hex Conversion"""
# The rgb function is incomplete. Complete it so that passing in RGB decimal values
# will values will result in a hexadecimal represntation being returned.
# Valid decimal values for RGB are 0-255. Any values that fall out of that range
# must be rounded to the closest valid value.

# Note: Your answer should always be 6 characters long, the shorthand with 3 will
# not work here. 

def rgb(*args):
    result = []

    for arg in args:
        if arg < 0:
            arg = 0
        elif arg > 255:
            arg = 255
        result.append(f"{arg:02X}")

    return "".join(result)

print(rgb(253, 43, 0))



