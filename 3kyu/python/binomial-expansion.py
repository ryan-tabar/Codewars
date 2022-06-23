"""3kyu: Binomial Expansion"""
# Link: https://www.codewars.com/kata/540d0fdd3b6532e5c3000b5b/train/python
# A function that takes in an expression and performs algebra on it and returns the result

# The expression is in the form (ax+b)^n
# a and b are integers which may be positive or negative
# x is any single character variable
# n is a natural number

# If a=1, no coefficient will be placed in front of the variable.
# If a=-1, a "-" willbe placed in front of the variable

# The expanded form should be returned as a string in the form
# ax^b + cx^d + ex^f ....

# If the coefficient of a term is 0, the term should not be included
# If the coefficient of a term is 1, the 1 should not be included
# If the coefficient of a term is -1, only the "-" should be included
# If the power of the term is 0, only the coefficient shoul dbe included
# If the power of the term is 1, the caret and power should be excluded

def pascal_row(n):
    """Return nth row of Pascal's Triangle as list"""
    if n == 0:
        return [1]
    if n == 1:
        return [1, 1]
    ls = [1, 1]
    temp = [1, 1]
    for i in range(2, n + 1):
        ls = temp
        temp = [1]
        for i in range(len(ls) - 1):
            temp.append(ls[i] + ls[i + 1])
        temp.append(1)
    return temp


def expand(expr):
    """Return Bionomial Expansion of input string"""
    import re

    # 1. Extract variables with the pattern of (ax+b)^n
    vars = re.match(r"\((-)?(\d+)?(\w)\+?(-?\d+)\)\^(\d+)", expr)

    # 2. Place groups into variables with the pattern (ax+b)^n
    a = int((vars[1] or "") + (vars[2] or "1"))
    x = vars[3]
    b = int(vars[4])
    n = int(vars[5])

    # Anything to the power of zero is 1
    if n == 0:
        return "1"

    if b == 0:
        coefficent = a**n
        if coefficent == 1:
            coefficent = ""
        elif coefficent == -1:
            coefficent = "-"
        return f"{coefficent}{x}^{n}"

    # 3. Perform binomial expansion
    result = ""
    # Iterate over Pascal's Triangle by using the powers of 11
    for i, pc in enumerate(pascal_row(n)):
        power = n - i
        coefficent = int(pc) * (b**i) * (a ** (power))

        if coefficent == 1:
            result += "+1" if power == 0 else "+"
        elif coefficent == -1:
            result += "-1" if power == 0 else "-"
        else:
            result += f"{coefficent:+}"

        if power == 1:
            result += x
        elif power > 1:
            result += f"{x}^{n-i}"

    # 4. Return result
    # If result starts with "+" remove it
    return result if result[0] == "-" else result[1:]


# Examples
print(expand("(x+1)^2"))  # expect: "x^2+2x+1"
print(expand("(p-1)^3"))  # expect: "p^3-3p^2+3p-1"
print(
    expand("(2f+4)^6")
)  # expect: "64f^6+768f^5+3840f^4+10240f^3+15360f^2+12288f+4096"
print(expand("(-2a-4)^0"))  # expect: "1"
print(expand("(-12t+43)^2"))  # expect: "144t^2-1032t+1849"
print(expand("(r+0)^203"))  # expect: "r^203"
print(expand("(-x-1)^2"))  # expect: "x^2+2x+1"
print(expand("(-5m+3)^4"))  # expect: "625m^4-1500m^3+1350m^2-540m+81"
