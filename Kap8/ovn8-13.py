def sgd(m, n):
    if m == n:
        return m
    elif m > n:
        return sgd(m-n, n)
    else:
        return sgd(m, n-m)
        
# Test
m = int(input('Det första talet: '))
n = int(input('Det första talet: '))
print(sgd(m,n))