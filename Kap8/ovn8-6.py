def rotera(l):
    e = l[-1]
    l[1:len(l)] = l[0:len(l)-1]
    l[0] = e

# Test
a = input('Skriv en lista: ').split()
print(a)
rotera(a)
print(a)
