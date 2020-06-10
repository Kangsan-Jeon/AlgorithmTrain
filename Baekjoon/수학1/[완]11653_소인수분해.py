import sys


def solve(num):
    if num == 1:
        return
    for i in range(2, num+1):
        if num%i == 0:
            print(i)
            return solve(num//i)
    return print(num)


def main():
    N = int(sys.stdin.readline())
    solve(N)


if __name__ == "__main__":
    main()