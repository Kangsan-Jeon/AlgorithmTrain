import sys

def solve(n, arr):
    table = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n-i):
            if j == j+i:
                table[j][j + i] = 1
            else:
                if table[]


    for i in range(n):
        print(table[i])
    return table[0][n-1]


def main():
    N = int(sys.stdin.readline())
    arr = [int(x) for x in sys.stdin.readline().split()]
    answer = solve(N, arr)
    print(answer)


if __name__ == "__main__":
    main()