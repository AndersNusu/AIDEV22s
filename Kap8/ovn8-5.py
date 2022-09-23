def rel_prim(i, j):
    k = 2
    while k<=i and k<=j:
        if i%k == 0 and j%k == 0:
            return False
        k += 1
    return True

# Test
a = int(input('Det första talet: '))
b = int(input('Det andra talet:  '))
if rel_prim(a, b):
    print('Relativa primtal')
else:
    print('Inte relativa primtal')