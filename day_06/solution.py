import os
import time

here = os.path.dirname(os.path.abspath(__file__))
input_filename = os.path.join(here, 'input.txt')

banks = []

with open(input_filename, 'r') as input_file:
    banks = [int(x) for x in input_file.read().strip().split('\t')]

num_banks = len(banks)

already_seen = ['_'.join([str(x) for x in banks])]

distributions = 0

goal_hash = None
part_b = False
while True:
    # Find highest bank
    highest = 0
    index = 0
    for i in range(0, num_banks):
        if banks[i] > highest:
            highest = banks[i]
            index = i

    # Distribute
    banks[index] = 0
    increment = index + 1
    while highest > 0:
        banks[increment % num_banks] += 1
        increment += 1
        highest -= 1

    # Hash and check
    bank_hash = ('_'.join([str(x) for x in banks]))

    distributions += 1

    if bank_hash in already_seen:
        if part_b == False:
            goal_hash = bank_hash
            print('Part A solution: {}'.format(distributions))
            part_b = True
            distributions = 0
        else:
            if bank_hash == goal_hash:
                print('Part B solution: {}'.format(distributions))
                break

    already_seen.append(bank_hash)
