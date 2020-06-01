import sys


def solve(answer, line):
    for char in line:
        decimal = ord(char)
        if 97 <= decimal <= 122:
            answer[0] += 1
        elif 65 <= decimal <= 90:
            answer[1] += 1
        elif 48 <= decimal <= 57:
            answer[2] += 1
        elif decimal == 32:
            answer[3] += 1
        else:
            pass
    print(*answer)


def main():
    for i in range(100):
        line = sys.stdin.readline()[:-1]
        if len(line) == 0:
            break
        else:
            solve([0, 0, 0, 0], line)


if __name__ == "__main__":
    main()
