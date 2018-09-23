def f(X):
    zeros = []
    # nullify rows and flag collumns indices with zeros
    for i in range(len(X)):
        for j in range(len(X[0])):
            if X[i][j] == 0:
                X[i] = [0] * len(X[0])
                zeros.append(j)
                break

    # nullify collumns
    for zero in set(zeros):
        for i in range(len(X)):
            X[i][zero] = 0
    return X

a = [[1, 2, 3],
    [4, 0, 6],
    [7, 8, 9],
   [10, 11, 12]]
b = [[1, 2, 3],
    [4, 5, 6],
    [7, 8, 0],
   [10, 11, 12]]
c = [[0, 2, 3],
    [4, 5, 6],
    ]

tests = [
        a,
        b,
        c
        ]

for test in tests:
    for i in f(test):
        print(i)
