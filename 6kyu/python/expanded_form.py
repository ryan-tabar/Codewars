"""6kyu: Write Number in Expanded Form"""

# You will be given a number and you will need to return it as a string
# in Expanded Form. For example:
# expanded_form(12) # Should return '10 + 2'
# expanded_form(42) # Should return '40 + 2'
# expanded_form(70304) # Should return '70000 + 300 + 4'

def expanded_form(input):
    result = []
    for i, digit in enumerate(str(input)[::-1]):
        if digit != "0":
            result.append(str(digit) + "0"*i)
    return " + ".join(result[::-1])

print(expanded_form(70304))