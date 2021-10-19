T = int(input())

def check(char):
    if char == "R" or char == "B" or char == "Y":
        return True
    else:
        return False

for _ in range(T):
    s = input()

    i = 0
    rolling = 0
    curr = []
    while i < len(s) - 1:
        if check(s[i]) and check(s[i+1]):
            rolling += 1
        else:
            if rolling != 0:
                curr.append(rolling + 1)
            rolling = 0

        i += 1

    if rolling != 0:
        curr.append(rolling + 1)

    total = 0
    for val in curr:
        total += (val * (val + 1)) // 2 - val

    print(total)