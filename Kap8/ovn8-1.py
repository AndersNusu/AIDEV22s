def pris(exkl_moms, proc):
    return exkl_moms * (1 + proc / 100)

# Test
x = float(input('Pris exkl moms: '))
p = float(input('Procent moms: '))
print(f'Pris inkl moms: {pris(x, p):.2f}')

