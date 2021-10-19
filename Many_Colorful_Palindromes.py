from collections import Counter
T = int(input())

for _ in range(T):
    N, K = map(int, input().split())

    char = []
    for __ in range(K):
        char.append(list(input()))

    count = [0] * N

    for i in range(N):
        col = []
        for j in range(K):
            col.append(char[j][i])
        count[i] = Counter(col)

    n = N // 2

    good = True
    for i in range(n):
        if dict(count[i].most_common()) == dict(count[-(i+1)].most_common()):
            continue
        else:
            good = False
    
    print("POSSIBLE" if good else "IMPOSSIBLE")