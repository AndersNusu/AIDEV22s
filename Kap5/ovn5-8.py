t1 = input('Första tidpunkten (tt:mm)? ')
t2 = input('Andra tidpunkten (tt:mm)?  ')
tim1 = int(t1[0:2])
min1 = int(t1[3:5])
tim2 = int(t2[0:2])
min2 = int(t2[3:5])
min1 += tim1 * 60
min2 += tim2 * 60
if min2 < min1:
    min2 += 24 * 60
print(f'Det har gått {min2-min1} minuter')