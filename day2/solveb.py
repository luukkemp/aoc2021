#!/usr/bin/env python3

hpos = 0
depth = 0
aim = 0
with open('input', 'r') as f:
    for line in f:
        line = line.rstrip()
        line = line.split(' ')
        d = line[0]
        n = int(line[1])
        if d == 'forward':
            hpos += n
            depth += (aim*n)
        if d == 'up':
            aim -= n
        if d == 'down':
            aim += n
print(hpos * depth)
