def palindrome_permutation(s):
    d = {}
    odds = 0
    s = ''.join(s.lower().split())
    for i in s:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    for i in d:
        if d[i] % 2 != 0:
            odds += 1
            if odds > 1:
                return False
    return True

s1 = "Taco  cat"
s2 = "cat"

print(palindrome_permutation(s1))
