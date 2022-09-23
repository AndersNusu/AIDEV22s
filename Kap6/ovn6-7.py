# Läs in taluppställningn
print('Skriv en matris rad för rad. ' 
      'Avsluta med en tom rad.')
m = []
while True:
    s = input('? ')
    if s == '':
        break
    ls = s.split()                # lista med texter
    rad = [float(e) for e in ls]  # lista med float
    m.append(rad)                 # ny rad i matrisen

# Kontollera att antalet rader och kolumner är lika
n = len(m)        # antal rader
for rad in m:
    if len(rad) != n:
        print('Inte magisk')
        exit()
summan = 0
# Beräkna summan i första diagonalen
for i in range(0, n):
    summan += m[i][i]
summan2 = 0
# Undersök summan i andra diagonalen
for i in range(0, n):
    summan2 += m[i][n-1-i]
if summan2 != summan:
    print('Inte magisk')
    exit()
# Undersök summan av varje rad
for rad in m:
    if sum(rad) != summan:
        print('Inte magisk')
        exit()
# Undersök summan av varje kolumn
for k in range(0, n):
    summan2 = 0
    for r in range(0, n):
        summan2 += m[r][k]
    if summan2 != summan:
        print('Inte magisk')
        exit()
print('Magisk')
    




