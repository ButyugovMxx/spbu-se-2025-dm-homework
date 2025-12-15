#!/usr/bin/env python3

n, m = map(int, input().split())
if n == 0:
    print("-"); print("-"); print("-"); print("-"); exit()

a = input().split()
idx = {a[i]: i for i in range(n)}
incoming = [[] for _ in range(n)]
outgoing = [[] for _ in range(n)]

for _ in range(m):
    x, y = input().split()
    incoming[idx[y]].append(idx[x])
    outgoing[idx[x]].append(idx[y])

mins = sorted(a[i] for i in range(n) if not incoming[i])
maxs = sorted(a[i] for i in range(n) if not outgoing[i])

print(" ".join(mins) if mins else "-")
print(" ".join(maxs) if maxs else "-")
print(mins[0] if len(mins) == 1 else "-")
print(maxs[0] if len(maxs) == 1 else "-")

