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


print(*sorted(mins))
print(*sorted(maxs))

if len(mins) == 1:
    print(mins[0])
else:
    print("-")

if len(maxs) == 1:
    print(maxs[0])
else:
    print("-")


