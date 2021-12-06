#!/usr/bin/env python3

hpos = 0
depth = 0
with open('input', 'r') as f:
    for line in f:
        line = line.rstrip()
        line = line.split(' ')
        d = line[0]
        n = int(line[1])
        if d == 'forward':
            hpos += n
        if d == 'up':
            depth -= n
        if d == 'down':
            depth += n
print(hpos * depth)
