import sys


def solve(n):
    table = [-1, 1, 3]
    for i in range(3, n+1):
        table.append(table[i - 1] + table[i - 2]*2)
    return table[n]


def main():
    n = int(sys.stdin.readline())
    answer = solve(n)
    print(answer%10007)


if __name__ == "__main__":
    main()