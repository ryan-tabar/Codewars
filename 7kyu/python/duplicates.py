"""7kyu: Remove duplicate words"""
# Your task is to remove all duplicate words from a string,
# leaving only single (first) words entries.

# Example:

# Input:
# 'alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta'

# Output:
# 'alpha beta gamma delta'

def remove_duplicate_words(s):
    return ' '.join(dict.fromkeys(s.split(' ')))

print(remove_duplicate_words('alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta'))