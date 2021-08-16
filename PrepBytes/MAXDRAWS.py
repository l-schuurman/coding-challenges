# Determine number of draws required at worst case to be guaranteed to select
# a matching pair of socks from a box full of socks

import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
  print(int(input()) + 1)