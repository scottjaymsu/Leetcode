'''
Time : O(n)
Space : O(1)
'''

def IsUnique(s):
    # edge case : only 128 unique ASCII characters
    if len(s) > 128:
        return False

    # bit vector
    # 1 == value has been seen before
    # initialize with 0s, assuming that only 128 ASCII chars
    seen = [0] * 128

    # iterate through string
    for c in s:
        # Converts character to ascii integer value
        idx = ord(c)
        # if character has already been seen and bit has been flipps
        if seen[idx] == 1:
            return False
        seen[idx] = 1

    return True

print(IsUnique("abc"))
print(IsUnique("aa"))
print(IsUnique(""))
print(IsUnique("  "))