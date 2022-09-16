största = 0
minsta = 1.e300   # ett stort tal
while True:
    tal = float(input('> '))
    if tal < 0:
        break
    if tal > största:
        största = tal
    if tal < minsta:
        minsta = tal
print(f'Största talet: {största}')
print(f'Minsta talet: {minsta}')