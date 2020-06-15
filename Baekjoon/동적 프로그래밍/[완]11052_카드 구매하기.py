import sys


def solve(N, packs):
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