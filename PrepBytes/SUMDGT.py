# Sum digits in number

import sys

input = sys.stdin.readline

x = input()

s = 0
for digit in x:
  s += int(digit)
  
print(s)