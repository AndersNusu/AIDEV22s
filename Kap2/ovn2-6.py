import math
t = int(input('Antal år? '))
lam = math.log(2.0) / 5730
n0 = 100   # 100 % från början
rest = n0 * math.exp(-lam * t)
print(f'Det återstår {rest:.1f} %')