N, M = map(int, input().split())
repairs = list(map(int, input().split()))
coupons = list(map(int, input().split()))

repairs.sort(reverse=True)
coupons.sort(reverse=True)

total = 0

length = len(repairs)
for i in range(length):
    if i < len(coupons):
        repairCost = max(0, repairs[i] - coupons[i])
    else:
        repairCost = repairs[i]

    total += repairCost

print(total)