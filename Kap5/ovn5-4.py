konsonanter = 'bcdfghjklmnpqrstvxz'
s = input('Skriv en text: ')
r = ''
for e in s:
    t = e.lower()
    if t in konsonanter:
        r += t + 'o' + t 
    else:
        r += t 
print(r)