'''
Time : O(n^2)
Space : O(n)
'''
def WorseCompressString(s):
    #edge case: invalid input/string for sure smaller than compression
    if s is None or len(s) < 2:
        return s

    ans = ""
    i,j = 0,1

    # iterate through string - O(n)
    while j < len(s):
        # new char found
        if s[i] != s[j]:
            ans += s[i] #< O(n) - strings are immutable so each char will need to be copied to new string
            ans += str(j-i)
            # new char location
            i = j
        j += 1

    # append remaining compressed characters
    ans += s[i]
    ans += str(j-i)

    # return string based on criteria (len(compression) < len(s))
    if len(ans) < len(s):
        return ans
    return s

'''
Time : O(n)
Space : O(n)
'''
def CompressString(s):
    if s is None or len(s) < 2:
        return s

    ans = []
    i, j = 0, 1

    # O(n)
    while j < len(s):
        if s[i] != s[j]:
            # O(1) amortized - list will double in size when capacity is reached
            # but appending operation is O(1) on average
            ans.append(s[i])
            ans.append(str(j - i))
            i = j
        j += 1

    ans.append(s[i])
    ans.append(str(j - i))

    # O(n)
    compressed = ''.join(ans)
    return compressed if len(compressed) < len(s) else s

print(CompressString("aabcccccaaa")) #< a2b1c5a3
print(CompressString("abc")) #< abc (compression is larger than input)
print(CompressString("ab")) #< ab (too small of input)
print(CompressString("")) #< invalid input
print(CompressString("AAbcccccaaA")) #< A2b1c5a2A1


