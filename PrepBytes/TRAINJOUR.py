# Determine seat across the aisle based on a given seat layout

import sys

input = sys.stdin.readline

berth = {
  1: "LB", 2: "MB", 3: "UB", 4: "LB", 5: "MB", 6: "UB", 7: "SU", 8: "SL"
}

seat = {
  1: 4, 2: 5, 3: 6, 4: 1, 5: 2, 6: 3, 7: 8, 8: 7
}

t = int(input())

for _ in range(t):
  n = int(input())
  nMod = n % 8 if n % 8 != 0 else 8
  print(n + seat[nMod] - nMod, berth[nMod], sep="")