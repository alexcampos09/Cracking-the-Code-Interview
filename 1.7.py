a = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
    ]
# answer = [
#     [3, 6, 9],
#     [2, 5, 8],
#     [1, 4, 7]
#     ]

tests = [a]

#left rotation
def f(X):
    return reversed([[X[j][i] for j in range(len(X))] for i in range(len(X[0]))])

for test in tests:
    for i in f(test):
        print(i)
