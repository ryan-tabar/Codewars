"""7kyu: Sum of the first nth term of Series"""

# Return the sum of the following series up to the nth term
# Series: 1 + 1/4 + 1/7 + 1/10 + 1/13 + 1/16 +...

# - Round the answer to 2 decimal places
# - 0 = 0.00
# - Arguments are only natural numbers

# Return as a string

def series_sum(n):
    return f"{sum(1/(3*i + 1) for i in range(n)):.2f}"


print(series_sum(5))
