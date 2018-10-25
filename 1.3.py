def URLify(s):
    return (s.lower().strip().replace(' ', '%'))

s1 = "Mr John Smith   "
s2 = "Mr John Smith"
s3 = "Cats and Dogs"

print(URLify(s1))
print(URLify(s2))
print(URLify(s3))
