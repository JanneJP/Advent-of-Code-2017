import os

here = os.path.dirname(os.path.abspath(__file__))
input_filename = os.path.join(here, 'input.txt')

phrases = []

with open(input_filename, 'r') as input_file:
    for line in input_file:
        tmp = line.strip().split(' ')
        phrases.append(tmp)

valid_phrases_a = 0

for phrase in phrases:
    invalid = False
    for i in range(0, len(phrase)):
        for j in range(0, len(phrase)):
            if i != j:
                if phrase[i] == phrase[j]:
                    invalid = True
    if not invalid:
        valid_phrases_a += 1

print('Solution part A: {}'.format(valid_phrases_a))

valid_phrases_b = 0

for phrase in phrases:
    invalid = False
    for i in range(0, len(phrase)):
        for j in range(0, len(phrase)):
            if i != j:
                if phrase[i] == phrase[j]:
                    invalid = True
                if ''.join(sorted(phrase[i])) == ''.join(sorted(phrase[j])):
                    invalid = True
                #if phrase[i] == phrase[j][::-1]:
                #    invalid = True
    if not invalid:
        valid_phrases_b += 1

print('Solution part B: {}'.format(valid_phrases_b))