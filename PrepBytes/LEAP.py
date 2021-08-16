# Determine if year is a leap year

import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
  year = int(input())
  
  print("Yes" if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0) else "No")