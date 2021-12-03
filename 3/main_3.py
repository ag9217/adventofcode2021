import numpy as np
from bit_criteria_func import bit_critera_func

# Gathering input data and creating integer list
data = open('input.txt').read().splitlines()

#--------------------PART 1--------------------#

gamma = ''

for digit in range(0, len(data[0])):
    count_0 = 0
    count_1 = 0

    for bin_num in data:
        if bin_num[int(digit)] == '1':
            count_1 = count_1 + 1
        elif bin_num[int(digit)] == '0':
            count_0 = count_0 + 1

    if count_1 > count_0:
        gamma = gamma + '1'
    else:
        gamma = gamma + '0'

print('Gamma (binary): ', gamma)
gamma_int = int('0b'+gamma, 2)
print('Gamma (decimal): ', gamma_int)

# Generating epsilon
epsilon = ""

for char in gamma:
    if char == '1':
        epsilon = epsilon + '0'
    else:
        epsilon = epsilon + '1'

print("Epsilon (binary): ", epsilon)
epsilon_int = int('0b'+epsilon, 2)
print("Epsilon (decimal): ", epsilon_int)

print("Gamma * Epsilon: ", gamma_int*epsilon_int)

#--------------------PART 2--------------------#

OGR = bit_critera_func(data, 0)
print(OGR)
