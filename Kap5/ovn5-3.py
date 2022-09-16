import datetime
nr = input('Skriv ett personnummer: ')
siff = int(nr[-2])
if siff % 2 == 0:
    print('Kvinna')
else:
    print('Man')