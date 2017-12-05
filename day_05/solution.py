import os

here = os.path.dirname(os.path.abspath(__file__))
input_filename = os.path.join(here, 'input.txt')

instructions = []
instructions_2 = []

with open(input_filename, 'r') as input_file:
    for line in input_file:
        instructions.append(int(line.strip()))
        instructions_2.append(int(line.strip()))

steps_1 = 0

current_position = 0
while True:
    try:
        next_instruction = instructions[current_position]
        next_position = current_position + next_instruction
        # Increment current instruction
        instructions[current_position] += 1

        current_position = next_position

        steps_1 += 1
    except IndexError as err:
        #print(str(err))
        break

print('Solution part A: {}'.format(steps_1))

steps_2 = 0

current_position = 0
while True:
    try:
        next_instruction = instructions_2[current_position]
        next_position = current_position + next_instruction
        # Increment current instruction
        if next_instruction >= 3:
            instructions_2[current_position] -= 1
        else:
            instructions_2[current_position] += 1

        current_position = next_position

        steps_2 += 1
    except IndexError as err:
        #print(str(err))
        break

print('Solution part B: {}'.format(steps_2))
