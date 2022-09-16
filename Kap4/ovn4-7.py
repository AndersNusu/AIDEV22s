n = int(input('Antal domare? '))
if n < 3:
    print('Felaktigt antal domare')
    exit()
while True:
    svårighet = float(input('Hoppets svårighetsgrad? '))
    if svårighet < 0:
        exit()
    sum = 0
    min_poäng = 10
    max_poäng = 0
    for i in range(1, n+1):
        domarpoäng = float(input(f'Poäng från domare nr {i}? '))
        if domarpoäng < 0:
            exit()
        sum += domarpoäng
        min_poäng = min(min_poäng, domarpoäng)
        max_poäng = max(max_poäng, domarpoäng)
    sum = sum - min_poäng - max_poäng
    hopp_poäng = sum / (n-2) * 3 * svårighet
    print(f'Hoppets poäng: {hopp_poäng:.3f}')
