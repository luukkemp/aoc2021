#!/usr/bin/env python3

l = []
with open('input', 'r') as f:
    for line in f:
        line = int(line.rstrip())
        l.append(line)

prevsum = -1
inc = 0
try:
    for i, n in enumerate(l):
        s = l[i] + l[i+1] + l[i+2]
        if prevsum > 0 and s > prevsum:
            inc += 1
        prevsum = s
except IndexError:
    pass
print(inc)
