def expo(x):
    epsilon = 1.0e-7
    sum = 0
    k = 0
    term = 1
    while abs(term) >= epsilon:
        sum += term
        k += 1
        term = term * x / k
    return sum

# Test
x = float(input('Skriv ett tal '))
print('expo ger:     ', expo(x))
import math
print('math.exp ger: ', math.exp(x))
