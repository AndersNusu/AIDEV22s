s = input('Skriv in de uppmätta temperatuerna: ')
ls = s.split()
temp = [float(e) for e in ls]
medel = sum(temp) / len(temp)
print(f'Medelvärde: {medel:.2f}')
print('Temperaturer högre än medelvärdet:')
for i in range(0, len(temp)):
    if temp[i] > medel:
        print(i+1, temp[i])