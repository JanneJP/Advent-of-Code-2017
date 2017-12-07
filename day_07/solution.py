import os

here = os.path.dirname(os.path.abspath(__file__))
input_filename = os.path.join(here, 'input.txt')

class Program(object):
    def __init__(self, name, weight, subs=None):
        self.name = name
        self.weight = int(weight)
        self.subs = subs


def parse_input(file_name):
    programs = []
    with open(file_name, 'r') as input_file:
        for line in input_file:
            tokens = line.strip().split(' -> ')
            first_token = tokens[0].split(' ')
            name = first_token[0]
            weight = first_token[1].replace('(', '').replace(')', '')
            subs = None
            if len(tokens) > 1:
                subs = tokens[1].split(', ')
            program = Program(name, weight, subs)
            programs.append(program)
    return programs

def find_trunk(p, l):
    for program in l:
        if program.subs != None and p.name in program.subs:
            return find_trunk(program, l)
    return p.name

programs = parse_input(input_filename)
rt = find_trunk(programs[0], programs)

print('Solution part A: {}'.format(rt))
