import sys


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def main():
    N, S = [int(x) for x in sys.stdin.readline().rstrip().split()]
    distances = [abs(int(x)-S) for x in sys.stdin.readline().rstrip().split()]
    answer = distances[0]

    for i in range(1, N):
        answer = min(answer, gcd(answer, distances[i]))
        if answer == 1:
            break

    print(answer)



if __name__ == "__main__":
    main()
