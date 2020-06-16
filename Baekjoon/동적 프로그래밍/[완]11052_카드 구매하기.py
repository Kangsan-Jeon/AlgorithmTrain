import sys


def solve(N, packs):
    '''
    table[1] = P1
    table[2] = min(P2, P(2-1) + P(1))
    table[3] = min(P3, P1 + P2, P2 + P1) => 뒤에 두개는 같은 것이므로 앞에 것만 고려
    table[4] = min(P4, P1 + P3, P2 + P2)
    table[5] = min(P5, P1 + P4, P2 + P3)
    '''
    table = [0]*(N+1)
    for i in range(1, N+1):
        temp = [packs[i-1]]
        for j in range(i//2):
            temp.append(table[i-j-1] + table[j+1])
        table[i] = max(temp)
    return table[N]


def main():
    N = int(sys.stdin.readline())
    packs = [int(x) for x in sys.stdin.readline().split()]
    print(solve(N, packs))


if __name__ == "__main__":
    main()