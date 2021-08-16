# Output triangle shape of numbers decreasing from n to 1

# EXAMPLE - n = 5
# 1 2 3 4 5
# 1 2 3 4
# 1 2 3
# 1 2
# 1

import sys

input = sys.stdin.readline

n = int(input())

for i in range(n, 0, -1):
  arr = list(range(1, i + 1))
  print(*arr)