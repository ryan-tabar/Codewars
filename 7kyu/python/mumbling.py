"""7kyu: Mumbling"""
# This time no story, no theory. The examples below show you how
# to write function accum: 

# accum("abcd") -> "A-Bb-Ccc-Dddd"
# accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
# accum("cwAt") -> "C-Ww-Aaa-Tttt"

def accum(s):
    return "-".join(c.upper() + i * c.lower() for i, c in enumerate(s))

print(accum("ZpglnRxqenU"))