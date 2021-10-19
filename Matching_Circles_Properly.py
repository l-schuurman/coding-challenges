from math import dist
from collections import defaultdict

N = int(input())
x = []
y = []
r = []

def find(x):
    if connected[x] == x: return x
    connected[x] = find(connected[x])
    return connected[x]

def union(u, v):
    u = find(u)
    v = find(v)
    if u == v: return
    connected[u] = v

for _ in range(N):
    xi, yi, ri = map(int, input().split())
    x.append(xi)
    y.append(yi)
    r.append(ri)

connected = [i for i in range(N)]

for i in range(N - 1): # Loop through circles
    for j in range(i + 1, N): # Check all circles for matches
        if connected[i] == connected[j]:
            continue
        else:
            d = dist((x[i], y[i]), (x[j], y[j]))
            if abs(r[i] - r[j]) <= d <= r[i] + r[j]:
                union(i, j)

print(len(set(find(i) for i in range(N))))

