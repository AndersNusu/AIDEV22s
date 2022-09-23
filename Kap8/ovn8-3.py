def små_stora(txt):
    små = 0
    stora = 0
    for e in txt:
        if e.islower():
            små += 1
        elif e.isupper():
            stora += 1
    return små, stora

# Test
s = input('Skriv en text: ')
a, b = små_stora(s)
print('Små:  ', a)
print('Stora:', b)