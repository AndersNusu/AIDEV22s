miles_per_g = float(input('Miles per gallon? '))
l_per_mil =  3.785 / miles_per_g / 1.609 * 10 
print(f'{l_per_mil:.2f} l/mil')