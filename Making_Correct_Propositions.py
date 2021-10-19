P = list(input())
Q = list(input())
func = input().split()

def solve(p, q, op):
    if op == "==":
        return int(p == q)
    elif op == "|":
        return p|q
    elif op == "&":
        return p&q
    elif op == "=>":
        return int(not(p) or q)
    elif op == "^":
        return p ^ q

res = []
for i in range(len(P)):
    p = int(P[i])
    q = int(Q[i])

    pq = solve(eval(func[0]), eval(func[2]), func[1])
    pq = solve(pq, eval(func[4]), func[3])

    res.append(str(pq))

print("".join(res))