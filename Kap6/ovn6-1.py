s = input('Skriv ett antal heltal: ')
ls = s.split()
tal = [int(e) for e in ls]
for i in range(0, len(tal)):
    if not tal[i] in tal[0:i]:
        print(tal[i], end=' ')