import math
ls = input('Skriv en vektor: ').split()
a = [float(e) ** 2 for e in ls]
l = math.sqrt(sum(a))
print(f'Längden blir: {l:0.2f}')