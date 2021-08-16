# Given three distinct integers, determine the middle integer

import sys

input = sys.stdin.readline

arr = list(map(int, input().split()))

print(sorted(arr)[1])