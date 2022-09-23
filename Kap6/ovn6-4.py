ls = input('Skriv in värden: ').split()
a = [float(e) for e in ls]
b = sorted(a)         # skapa en sorterad kopia
n = len(b) 
if n % 2 != 0:
    print(b[(n-1)//2])                # udda antal element
else:
    print((b[n//2-1] + b[n//2]) / 2)  # jämnt antal element