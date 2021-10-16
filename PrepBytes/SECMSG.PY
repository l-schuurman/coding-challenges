# Filter only uppercase letters and digits

t = int(input())
for _ in range(t):
    s = input()
    result = []

    for char in s:
        if char.isupper() or char.isdigit():
            result.append(char)

    print("".join(result))