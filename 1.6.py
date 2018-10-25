def rle(s):
    if len(set(s)) > len(s)/2:
        return s
    l = []
    prev = None
    count = 1
    for curr in s:
        if prev == curr:
            count += 1
        elif prev != None:
            l += prev + str(count)
            count = 1
        prev = curr
    l += prev + str(count)
    return ''.join(l)

s = 'aabcccccaaaßß'
s2 = 'abcd'

print(rle(s))
print(rle(s2))
