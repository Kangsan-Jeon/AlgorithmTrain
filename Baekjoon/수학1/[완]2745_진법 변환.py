import sys

# A(65) ~ Z(90)

dic = dict()
for i in range(10):
    dic[str(i)] = i
for i in range(26):
    dic[chr(65+i)] = 10 + i


def convert(n, b):
    answer = 0
    length = len(n)
    b = int(b)
    idx = 1
    for x in n:
        answer += dic[x]*(b**(length - idx))
        idx += 1
    return answer


def main():
    N, B = sys.stdin.readline().rstrip().split()
    print(convert(N, B))


if __name__ == "__main__":
    main()