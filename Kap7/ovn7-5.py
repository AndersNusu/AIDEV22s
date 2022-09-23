# Eratosthenes såll
n = int(input('Största tal? '))
a = [False] + [True] * n           # index från 0 till n
for i in range(2, len(a)):
    if a[i]:
        for j in range(i+1, len(a)):
            if j % i == 0:
                a[j] = False
primtal = []
for k in range (0, len(a)):
    if a[k]:
        primtal.append(k)
print(f'Primtalen <= {n:d} är:')
print(primtal)