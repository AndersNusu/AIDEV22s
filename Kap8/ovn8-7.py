def nfak(n):
    r = 1
    for i in range(2, n+1):
        r = r * i
    return r

def binkoeff(n, k):
    return nfak(n) // (nfak(k) * nfak(n-k))

# Test
n = int(input('n? '))
k = int(input('k? '))
print(binkoeff(n, k))
