import sys


def main():
    binary = list(sys.stdin.readline().rstrip())
    answer = ""
    length = len(binary)
    for i in range(length//3):
        temp = 0
        for j in range(3):
            temp += int(binary.pop())*(2**j)
        answer = str(temp) + answer

    if len(binary) != 0:
        idx = 0
        temp = 0
        while len(binary) != 0:
            temp += int(binary.pop())*(2**idx)
            idx += 1
        answer = str(temp) + answer
    print(answer)


if __name__ == "__main__":
    main()