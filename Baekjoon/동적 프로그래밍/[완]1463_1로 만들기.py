import sys

MAX = 1000000


def solve(N, arr):
    for i in range(1, N+1):
        if arr[i] > arr[i-1] + 1:
            arr[i] = arr[i-1] + 1
        if i%2 == 0 and arr[i] > arr[i//2] + 1:
            arr[i] = arr[i//2] + 1
        if i%3 == 0 and arr[i] > arr[i//3] + 1:
            arr[i] = arr[i//3] + 1
    return arr[N]


def main():
    N = int(sys.stdin.readline())
    arr = [MAX for _ in range(MAX + 1)]
    arr[1] = 0
    print(solve(N, arr))


if __name__ == "__main__":
    main()