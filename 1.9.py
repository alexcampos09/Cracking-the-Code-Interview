def f(s1, s2):
    return s1 in s2 + s2 or s2 in s1 + s1

tests = [
        ("cat", "tatctaca"),
        ("attacat", "cat"),
        ("cat", "taca"),
        ("cat", "atc"),
        ("cat", "atckcc"),
        ("waterbottle", "erbottlewat"),
        ("waterbottll", "erbottlewat"),
]
for test in tests:
    print(f(test[0], test[1]))
