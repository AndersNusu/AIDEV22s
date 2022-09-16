min = int(input('Antal minuter per månad? '))
if min  <= 33:
    print('Välj Kontant')
elif min > 33 and min  <= 66:
    print('Välj Normal')
else:
    print('Välj Plus')