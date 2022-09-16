import math
a = float(input('Längden för första sidan? '))
b = float(input('Längden för andra sidan? '))
v = float(input('Vinkeln mellan sidorna? '))
alfa = v * 2 * math.pi / 360     # omräkning till radianer
c = math.sqrt(a**2 + b**2 - 2*a*b*math.cos(alfa))
e = 1e-10    # ett litet tal
if abs(a-b) < e and abs(a-c) < e and abs(b-c) < e:
    print('Liksidig')
elif abs(a-b) < e or abs(a-c) < e or abs(b-c) < e:
    print('Likbent')
else:
    print('Oliksidig')