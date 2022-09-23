m = int(input('Första talet? '))
n = int(input('Andra talet? '))
while True:
    r = m % n
    if r == 0:
        break
    m = n
    n = r   
print(f'Största gemensamma delare är {n}')