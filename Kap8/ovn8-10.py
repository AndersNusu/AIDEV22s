def korrekt(a):
    # Kolla siffrorna på raderna
    for rad in a:
        antal = [0] * 9
        for siff in rad:
            if siff>=1 and siff <=9:
                antal[siff-1] += 1
        if antal != [1] * 9:
            return False
    # Kolla siffrorna i kolumnerna
    for kol in range(0, 9):
        antal = [0] * 9
        for r in range(0, 9):
            siff = a[r][kol]
            if siff>=1 and siff <=9:
                antal[siff-1] += 1
        if antal != [1] * 9:
            return False
    # Kolla siffrorna i regionerna
    for m in range(0, 3):
        for n in range(0, 3):
            # Undersök region m X n
            antal = [0] * 9            
            for i in range(m*3, (m+1)*3):
                for j in range(n*3, (n+1)*3):
                    siff = a[i][j]            
                    if siff>=1 and siff <=9:
                        antal[siff-1] += 1
            if antal != [1] * 9:
                return False
    return True

# Test. En korrekt lösning:
a = [[4, 8, 3, 9, 2, 1, 6, 5, 7],
     [9, 6, 7, 3, 4, 5, 8, 2, 1],
     [2, 5, 1, 8, 7, 6, 4, 9, 3],
     [5, 4, 8, 1, 3, 2, 9, 7, 6],
     [7, 2, 9, 5, 6, 4, 1, 3, 8],
     [1, 3, 6, 7, 9, 8, 2, 4, 5],
     [3, 7, 2, 6, 8, 9, 5, 1, 4],
     [8, 1, 4, 2, 5, 3, 7, 6, 9],
     [6, 9, 5, 4, 1, 7, 3, 8, 2]]

print(korrekt(a))