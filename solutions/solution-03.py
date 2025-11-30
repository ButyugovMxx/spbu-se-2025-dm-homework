#!/usr/bin/env python3
from collections import deque

n, m = map(int, input().split())
elements = input().split()

graph = {x: [] for x in elements}
in_deg = {x: 0 for x in elements}

for _ in range(m):
    u, v = input().split()
    graph[u].append(v)
    in_deg[v] += 1

# Очередь для вершин с нулевой входящей степенью
queue = deque(sorted([x for x in elements if in_deg[x] == 0]))
topo_order = []
pos = 1
result = {}

while queue:
    u = queue.popleft()
    topo_order.append(u)
    result[u] = pos
    pos += 1
    for v in sorted(graph[u]):  # сортируем для лексикографического порядка
        in_deg[v] -= 1
        if in_deg[v] == 0:
            queue.append(v)

# Выводим элементы в порядке топологической сортировки с их номерами
for x in topo_order:
    print(x, result[x])
