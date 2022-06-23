"""7kyu: Breaking chocolate problem"""
# Your task is to split the chocolate bar of given dimension nxm
# into small squares. Each square is size 1x1 and unbreakable.
# Implement a function that will return minimum number of breaks needed.

# For example if you are given a chocolate bar of size 2x1 you can split
# it to single squares in just one break, but for size 3x1 you must do two breaks.

# If input data is invalid you should return 0 (as in no breaks are needed) if we
# do not have any chocolate to split). Input will always be a non-negative integer.


def breakChocolate(n, m):
    return 0 if m == 0 or n == 0 else min(m, n) * max(m, n) - 1
