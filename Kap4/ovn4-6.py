term = 1.0
sum = 1.0
tecken = 1
k = 1
while abs(term) >= 1.0e-5:
    k += 1
    tecken = - tecken
    term = tecken * 1/k
    sum += term
print(f'Summan blir {sum}')