from collections import Counter
from math import comb

N = int(input())
cards = list(map(int, input().split()))

count = Counter(cards)

dupl = 0
for card in count:
    dupl += comb(count[card], 2)

total = comb(len(cards), 2)

print(dupl / total)
