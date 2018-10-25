s1 = 'alalu'
s2 = 'alula'
s3 = 'cat'
s4 = 'god '
s5 = 'Dog  '

def is_permutation(s1, s2):
    if len(s1.strip()) != len(s2.strip()):
        return False
    return sorted(s1.lower().strip()) == sorted(s2.lower().strip())

print(is_permutation(s4, s5))
