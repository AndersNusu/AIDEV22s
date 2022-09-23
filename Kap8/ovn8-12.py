def lön(år):
    if år <= 1:
        return 25000
    else:
        return lön(år-1) * 1.03 + 900

# Test
n = int(input('År? '))
print(lön(n))