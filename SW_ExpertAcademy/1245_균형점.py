T = int(input())

def calc(p1, p2, m1, m2):
    if m1 != m2:
        a = m1-m2
        b = p1*m2 - p2*m1
        c = m1*(p2**2) - m2*(p1**2)
        result1 = (-b + (b ** 2 - a * c) ** (1 / 2)) / a
        result2 = (-b - (b ** 2 - a * c) ** (1 / 2)) / a
        if (result1 > p1 and result1 < p2):
            result = result1
        else:
            result = result2
    else:
        result = (p1+p2)/2
    return result


for i in range(T):
    N = int(input())
    inp = input().split()
    pos = []
    mass = []
    result = []
    for j in range(N):
        pos.append(int(inp[j]))
        mass.append(int(inp[N+j]))
    for k in range(N-1):
        res = calc(pos[k], pos[k+1], mass[k], mass[k+1])
        result.append(res)
    print("#{}".format(i+1), end = " ")
    for r in result:
        print("{:.10f}".format(r), end = " ")
    print("")
