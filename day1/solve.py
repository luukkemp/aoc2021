#!/usr/bin/env python3

prev = 0
inc = 0
with open('input', 'r') as f:
    for line in f:
        line = int(line.rstrip())
        if line > prev:
            inc += 1
        prev = line

print(inc - 1)
