import os

here = os.path.dirname(os.path.abspath(__file__))
input_filename = os.path.join(here, 'input.txt')

instructions = None

with open(input_filename, 'r') as input_file:
    instructions = input_file.read().strip()

summed_1 = 0

for i in range(0, len(instructions)):
    try:
        if int(instructions[i]) == int(instructions[(i + 1)]):
            summed_1 += int(instructions[i])
    except IndexError as err:
        if int(instructions[i]) == int(instructions[0]):
            summed_1 += int(instructions[i])

double_instructions = instructions + instructions

summed_2 = 0
offset = int(len(instructions) / 2)

for i in range(0, len(instructions)):
    if int(double_instructions[i]) == int(double_instructions[(i + offset)]):
        summed_2 += int(instructions[i])

print('Part A solution: {}'.format(summed_1))
print('Part B solution: {}'.format(summed_2))
