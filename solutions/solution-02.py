#!/usr/bin/env python3
def bubble_sort(arr):
    arr = arr[:]
    n = len(arr)
    for i in range(n):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


n, m = map(int, input().split())
if n == 0:
    print("-")
    print("-")
    exit()

a = input().split()
idx = {a[i]: i for i in range(n)}

incoming = [[] for _ in range(n)]
outgoing = [[] for _ in range(n)]

for _ in range(m):
    x, y = input().split()
    incoming[idx[y]].append(idx[x])
    outgoing[idx[x]].append(idx[y])

#нет входящих рёбер
mins = [a[i] for i in range(n) if not incoming[i]]
#нет исходящих рёбер
maxs = [a[i] for i in range(n) if not outgoing[i]]

mins = bubble_sort(mins)
maxs = bubble_sort(maxs)

print(" ".join(mins) if mins else "-")
print(" ".join(maxs) if maxs else "-")
print(mins[0] if len(mins) == 1 else "-")
print(maxs[0] if len(maxs) == 1 else "-")
