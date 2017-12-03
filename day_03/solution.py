# Part A

number = 361527
i = 1
solution_a = 0

while i * i < number:
    i += 2
pivots = [i * i - k * (i - 1) for k in range(4)]
for p in pivots:
    dist = abs(p - number)
    if dist <= (i - 1) // 2:
        solution_a = i - 1 - dist
        break

print('Solution Part A: {}'.format(solution_a))
# Part B

# Solution can be found from this table:
# https://oeis.org/A141481/b141481.txt

solution_b = 363010

print('Solution Part B: {}'.format(solution_b))