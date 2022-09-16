konsonanter = 'bcdfghjklmnpqrstvxz'
s = input('Skriv rövarspråk: ')
i = 0
while i < len(s):
    print(s[i], end='')
    t = s[i].lower()
    if t in konsonanter:
        i += 3
    else:
        i += 1