antal_dagar = 1
dagens_lön = 0.01
totalt_belopp = 0.01 
while totalt_belopp < 10_000_000:
    antal_dagar += 1
    dagens_lön *= 2
    totalt_belopp = totalt_belopp + dagens_lön
print(f'Du måste arbeta {antal_dagar} dagar')