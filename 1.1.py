def is_unique(s):
    return len(s) == len(set(s))

s1 = 'catß'
s2 = 'catt'

print(is_unique(s1))
print(is_unique(s2))
