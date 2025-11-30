#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000)

n, m = map(int, input().split())

s = input().split()
a = []
for x in s:
    a.append(x)

idx = {a[i]: i for i in range(n)}

incoming = [[] for _ in range(n)]
outgoing = [[] for _ in range(n)]

for _ in range(m):
    x, y = input().split()
    ix = idx[x]
    iy = idx[y]
    outgoing[ix].append(iy)  
    incoming[iy].append(ix)

mins = [a[i] for i in range(n) if len(incoming[i]) == 0]
maxs = [a[i] for i in range(n) if len(outgoing[i]) == 0]


if mins:
    print(*sorted(mins))
else:
    print("-")

if maxs:
    print(*sorted(maxs))
else:
    print("-")

# сколько вершин достижимо из start (кроме самого start)
def reachable_count_from(start):
    seen = [False]*n
    stack = [start]
    seen[start] = True
    cnt = 0
    while stack:
        v = stack.pop()
        for w in outgoing[v]:
            if not seen[w]:
                seen[w] = True
                cnt += 1
                stack.append(w)
    return cnt

#сколько вершин доходят до target (через обратный граф incoming)
def reaches_count_to(target):
    seen = [False]*n
    stack = [target]
    seen[target] = True
    cnt = 0
    while stack:
        v = stack.pop()
        for w in incoming[v]:
            if not seen[w]:
                seen[w] = True
                cnt += 1
                stack.append(w)
    return cnt

# наименьший должен быть ровно один минимальный и из него достижимы все остальные
if len(mins) == 1:
    cand = mins[0]
    if reachable_count_from(idx[cand]) == n-1:
        print(cand)
    else:
        print("-")
else:
    print("-")

# наибольший ровно один максимальный и все остальные доходят до него
if len(maxs) == 1:
    cand = maxs[0]
    if reaches_count_to(idx[cand]) == n-1:
        print(cand)
    else:
        print("-")
else:
    print("-")
