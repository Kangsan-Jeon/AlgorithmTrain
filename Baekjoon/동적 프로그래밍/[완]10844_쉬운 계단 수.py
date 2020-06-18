import sys

REM = 1000000000

def solve(n):
    table = [[0 for _ in range(10)] for _ in range(100)]
    table[0] = [0, 1, 1, 1, 1,
                1, 1, 1, 1, 1]
    for i in range(1, n):
        table[i][0] = table[i-1][1] % REM
        table[i][9] = table[i-1][8] % REM
        for j in range(1, 9):
            table[i][j] = (table[i-1][j-1] + table[i-1][j+1]) % REM
    # print(table[n-1])
    return sum(table[n-1]) % REM


def main():
    N = int(sys.stdin.readline())
    answer = solve(N)
    print(answer % REM)


if __name__ == "__main__":
    main()