#!/usr/bin/env python3

import struct

g = ''
n = []
total = 0
with open('input', 'r') as f:
    for line in f:
        line = line.rstrip()
        if len(n) == 0:
            n = [0 for x in line]
        total += 1
        for i in range(len(n)):
            n[i] += int(line[i])
for i in range(len(n)):
    n[i] = round(n[i] / total)
gamma_string = ''.join([str(x) for x in n])
epsilon_string = ''.join([str(int(not (int(x)))) for x in n])
gamma = (int(gamma_string, 2))
epsilon = (int(epsilon_string, 2))
print(gamma * epsilon)
