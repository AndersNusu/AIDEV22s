n = int(input('Skriv ett positiv heltal: '))
print(f'Alla primtal <= {n}:')
for talet in range(1, n+1):
    är_primtal = True
    for k in range(2, talet):
        if talet % k == 0:
            är_primtal = False
    if är_primtal:
        print(talet)