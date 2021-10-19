# MCPC 2021 Tryouts

# Currently 10/15 points

from math import log10
from collections import Counter

n = int(input())
arr = list(map(float, input().split()))
count = Counter(arr)

a = b = 1
for val in count:
    a *= count[val] * abs(log10(val)) # alpha
    b *= count[val] * abs(log10(1 - val)) # beta

# With raw probabilities larger alpha wins (answer is 0)
# With log probabilities smaller alpha wins (answer is 0)

print(0 if a < b else 1)