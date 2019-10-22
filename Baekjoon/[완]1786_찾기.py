'''
Algorithm
[KMP]
'''
def makeTable(P):
    table = [0 for _ in range(len(P))]
    j = 0
    for i in range(1, len(P)):
        while (j > 0 and P[i] != P[j]):
            j = table[j-1]
        if P[i] == P[j]:
            j += 1
            table[i] = j
    return table

def solve(T, P):
    table = makeTable(P)
    j = 0
    cnt = 0
    pos = []
    for i in range(len(T)):
        while (j > 0 and T[i] != P[j]):
            j = table[j-1]
        if T[i] == P[j]:
            j += 1
        if j == len(P):
            cnt += 1
            pos.append(i-len(P)+2)
            j = table[len(P)-1]
    return cnt, pos

def main():
    T = input()
    P = input()
    cnt, pos = solve(T, P)
    print(cnt)
    print(*pos)

if __name__ == "__main__":
    main()