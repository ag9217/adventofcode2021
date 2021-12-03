import numpy as np

# Gathering input data and creating integer list
data = open('input.txt').read().splitlines()

#--------------------PART 1&2--------------------#
# horizontal, depth
position = [0, 0, 0]

for command in data:
    split_message = command.partition(" ")
    dir = split_message[0]
    mag = int(split_message[2])

    if dir == "forward":
        position[0] = position[0] + mag
        position[1] = position[1] + position[2] * mag
    elif dir == "down":
        position[2] = position[2] + mag
    elif dir == "up":
        position[2] = position[2] - mag

print(position)
print(position[0] * position[1])