from collections import Counter
T = int(input())

for _ in range(T):
    N, K = map(int, input().split())

    char = []
    for __ in range(K):
        char.extend(list(input()))

    count = Counter(char)

    odd = even = 0
    oddTotal = 0

    for char in count:
        if count[char] % 2 == 0:
            even += 1
        else:
            odd += 1
            oddTotal += count[char]

    # Note N*K is the total # of characters

    # If even length strings, no odd frequency of characters allowed
    if N % 2 == 0 and odd != 0: 
        print("IMPOSSIBLE")

    # Even pairs of characters can redistribute themselves in the center
    # unless there is an odd number of remaining spaces
    elif (K - odd) % 2 == 1:
        print("IMPOSSIBLE")

    # Having mooe odd characters than strings would fail
    elif K - odd < 0:
        print("IMPOSSIBLE")

    # Otherwise, it is possible to rearrange.
    else:
        print("POSSIBLE")
