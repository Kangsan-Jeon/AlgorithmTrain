import sys


def convert(a, b,inputs, m):
    return_b = []
    num = 0
    for i in range(m):
        num += inputs[i]*(a**(m-1-i))
    while num != 0:
        return_b.append(num%b)
        num = num//b
    return return_b


def main():
    A, B = [int(x) for x in sys.stdin.readline().rstrip().split()]
    m = int(sys.stdin.readline())
    inputs = [int(x) for x in sys.stdin.readline().rstrip().split()]
    answer = convert(A, B, inputs, m)
    length = len(answer)
    for i in range(length):
        print(answer[length-1-i], end=" ")


if __name__ == "__main__":
    main()