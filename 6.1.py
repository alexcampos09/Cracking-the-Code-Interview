def exp(n):
    l = [(n-1)*(0.5**n) for n in range(1,n)]
    print(l)
    return sum(l)

print(exp(6))
