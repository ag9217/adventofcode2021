import numpy as np

# Gathering input data and creating integer list
data = open('input.txt').read().splitlines()
data = list(map(int, data))

#--------------------PART 1--------------------#

# Variable to keep track of increases in depth
increases = 0

for i in range(1, len(data)-1):
    if data[i] - data[i-1] > 0:
        increases = increases + 1
    else:
        pass

print("Increases: ", increases)

#--------------------PART 2--------------------#

window_increases = 0

for i in range(0, len(data)-3):
    # Calculating sum of windows
    windowA = data[i] + data[i+1] + data[i+2]
    windowB = data[i+1] + data[i+2] + data[i+3]

    if windowB > windowA:
        window_increases = window_increases + 1
    else:
        pass

print("Window increases: ", window_increases)