def roten(x):
    epsilon = 1e-6
    g = x
    g_ny = x / 2   # första gissning
    while abs(g-g_ny) > epsilon:
        g = g_ny
        g_ny = (g + x/g)/2
    return g_ny

# Test
x = float(input('Skriv ett tal: '))
print('min funktion ger: ', roten(x))
import math
print('math.sqrt ger:    ', math.sqrt(x))