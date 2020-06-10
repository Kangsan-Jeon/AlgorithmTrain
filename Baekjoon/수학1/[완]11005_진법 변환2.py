import sys

# A(65) ~ Z(90)

dic = dict()
for i in range(36):
    if i < 10:
        dic[i] = str(i)
    else:
        dic[i] = chr(i + 55)


def convert(n, b):
    answer = ""
    while n != 0:
        rem = n%b
        n = n//b
        answer = dic[rem] + answer
    return answer


def main():
    N, B = [int(x) for x in sys.stdin.readline().rstrip().split()]
    print(convert(N, B))


if __name__ == "__main__":
    main()