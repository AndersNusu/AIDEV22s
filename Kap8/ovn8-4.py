def primtal(talet):
    är_primtal = True
    for k in range(2, talet):
        if talet % k == 0:
            är_primtal = False
    return är_primtal

# Test
t = int(input('Skriv ett tal: '))
if primtal(t):
    print('Primtal')
else:
    print('Ej primtal') 