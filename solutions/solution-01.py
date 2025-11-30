#!/usr/bin/env python3


nm = input().split()
Nn = int(nm[0])
Mm = int(nm[1])


s = input().split()  
a = s


r = []
for _ in range(Mm):
    aa, b = input().split()
    r.append((aa, b))

R = 'R'
S = 'S'
T = 'T'
A = 'A'

for x in a:
    if (x, x) not in r:
        R = '*'

for (x, y) in r:
    if (y, x) not in r:
        S = '*'

for (x, y) in r:
    for (u, v) in r:
        if y == u and (x, v) not in r:
            T = '*'

for (x, y) in r:
    if x != y and (y, x) in r:
        A = '*'

print(R + S + T + A)