# Determine who rolls the larger number more times

import sys

input = sys.stdin.readline

n = int(input())

pragya = 0
tina = 0

for _ in range(n):
  p, q = map(int, input().split())
  if p > q:
    pragya += 1
  elif p < q:
    tina += 1
    
if pragya > tina:
  print("Pragya")
elif pragya < tina:
  print("Tina")
else:
  print("Draw")