s = input('Skriv ett personnummer: ')
k = s.find('-')
if k != 6 or len(s) != 11:
    print("Felaktigt format. Längd eller '-'.")
    exit()
s = s.replace('-', '')       # ta bort tecknet -
# beräkna kontrollsumman
sum = 0
for i in range(0, len(s)-1):
    if not s[i].isdecimal():
        print('Felaktigt format. Inte siffror.')
        exit()
    tal = int(s[i])
    j = tal * (2-i%2)         # multiplicera med 2 eller 1
    sum += j//10 + j%10       # addera siffrorna i resultatet till summan
if (int(s[9]) + sum) % 10 == 0:
    print('Korrekt personnummer')
else:
   print('Felaktigt personnummer')