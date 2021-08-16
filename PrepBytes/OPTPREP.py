# Find the relation between X and Y

import sys

input = sys.stdin.readline

x, y = map(int, input().split())

if x > y:
  print(x, "is greater than", y)
elif x < y:
  print(x, "is smaller than", y)
else:
  print(x, "is equal to", y)