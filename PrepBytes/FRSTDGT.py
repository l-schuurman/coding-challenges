# Find the first digit of a number

import sys

input = sys.stdin.readline

t = int(input())

# METHOD 1 - numerically
for _ in range(t):
    n = int(input())

    while n >= 10:
        n //= 10

    print(n)

# METHOD 2 - string indexing
for _ in range(t):
    n = input()

    print(n[0])