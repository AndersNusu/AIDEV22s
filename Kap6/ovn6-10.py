ls = input('Skriv den första vektorn: ').split()
u = [float(e) for e in ls]
ls = input('Skriv den andra vektorn: ').split()
v = [float(e) for e in ls]
if len(u) != len(v):
    print('Olika antal element')
    exit()
summan = 0
for k in range(0, len(u)):
    summan += u[k] * v[k]
if summan == 0:
    print('Ortogonala')
else:
    print('Inte ortogonala')