import math
år = int(input('Vilket år? '))
antal = 26_000
for i in range(2020, år+1):
    antal = antal + math.ceil(300 - 325 + antal*(0.7-0.6)/100)
print(f'Beräknad befolkning: {antal}')