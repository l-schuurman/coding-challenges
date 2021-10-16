# Determine number of pairs (i, j) where A[i] = B[C[i]]

from collections import Counter, defaultdict

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = [x - 1 for x in list(map(int, input().split()))] # Account for non-zero indexing

# Count occurences of each value in C
cCount = Counter(C)

# Map all indexes of each value in B
bList = defaultdict(list)
for i, val in enumerate(B):
    bList[val].append(i)

total = 0
for Aval in A:
    for Bval in bList[Aval]:
        total += cCount[Bval] # Increment # of times B index occurs in C

print(total)