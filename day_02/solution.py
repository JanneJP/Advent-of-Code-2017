import os

here = os.path.dirname(os.path.abspath(__file__))
input_filename = os.path.join(here, 'input.txt')

# Part A

checksum_a = 0

with open(input_filename, 'r') as input_file:
    for line in input_file:
        tmp = line.rstrip().split('\t')

        values = []

        for val in tmp:
            values.append(int(val))
        
        minimum = None
        maximum = None

        for val in values:
            if minimum == None or val < minimum:
                minimum = val
            if maximum == None or val > maximum:
                maximum = val

        difference = maximum - minimum
        checksum_a += difference

print('Part A answer: {}'.format(checksum_a))

# Part B

checksum_b = 0

with open(input_filename, 'r') as input_file:
    for line in input_file:
        tmp = line.rstrip().split('\t')

        values = []

        for val in tmp:
            values.append(int(val))

        for val_1 in values:
            for val_2 in values:
                if val_1 / val_2 % 1 == 0 and val_1 != val_2:
                    checksum_b += int(val_1 / val_2)

print('Part B answer: {}'.format(checksum_b))