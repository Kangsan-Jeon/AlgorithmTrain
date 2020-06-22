import sys


def solve(n, arr):
    table = [1 for _ in range(n)]
    for i in range(n):
        for j in range(i):
            if arr[i] > arr[j]:
                table[i] = max(table[i], table[j] + 1)
    return max(table)

def main():
    N = int(sys.stdin.readline())
    arr = [int(x) for x in sys.stdin.readline().split()]
    answer = solve(N, arr)
    print(answer)


if __name__ == "__main__":
    main()