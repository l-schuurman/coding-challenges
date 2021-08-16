# Count the occurences of the digit five in each number
import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
  n = input()
  
  count = 0
  for digit in n:
    if digit == '5':
      count += 1
      
  print(count)